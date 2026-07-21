import os
import sys
import json
import uuid
import secrets
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
import anthropic

load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
client = anthropic.Anthropic()

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "questioner_prompt.txt", encoding="utf-8") as f:
    questioner_prompt = f.read()

with open(BASE_DIR / "evaluator_prompt.txt", encoding="utf-8") as f:
    evaluator_prompt = f.read()

with open(BASE_DIR / "summarizer_prompt.txt", encoding="utf-8") as f:
    summarizer_prompt = f.read()

sys.path.insert(0, str(BASE_DIR / "RAG_5-9"))
from database_engine import ContextualVectorDB

RAG_DB_PATH = str(BASE_DIR / "RAG_5-9" / "data" / "my_contextual_db" / "contextual_vector_db.pkl")
rag_db = ContextualVectorDB("my_contextual_db", db_path=RAG_DB_PATH)
rag_db.load_db()

ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")

# Session store: session_id -> {messages, turns, current_question, rag_contexts, evaluation_summary}.
# Persisted to SESSIONS_FILE after every mutation and reloaded at startup, so a
# restart doesn't lose history — this also doubles as the data source for the
# /admin/sessions endpoints below. Requires a single gunicorn worker: each
# worker would otherwise keep its own in-memory copy and clobber the others'
# writes to disk.
SESSIONS_FILE = BASE_DIR / "sessions.json"
try:
    with open(SESSIONS_FILE, "r", encoding="utf-8") as f:
        sessions = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    sessions = {}

def save_sessions():
    with open(SESSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(sessions, f, ensure_ascii=False, indent=2)

INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but explain what it is for the mean to be a model?"

# Conversation starter so the model sees the initial question in its history
BASE_MESSAGES = [
    {"role": "assistant", "content": INITIAL_MESSAGE},
]


def get_rag_context(query: str, k: int = 4) -> list[str]:
    # RAG embeddings run through Ollama over an SSH tunnel to a remote
    # research machine — treat that link as unreliable and degrade to no
    # context rather than 500ing the student's turn if it's down.
    try:
        results = rag_db.search(query, k=k)
    except Exception as exc:
        print(f"RAG lookup failed, continuing without context: {exc}")
        return []
    # contextualized_content is a retrieval aid baked into the embedding, not
    # something the model needs to read — only the source text goes in the
    # prompt. Dedup guards against near-identical/overlapping chunks (from
    # the chunker's sliding window) landing in the same top-k result.
    seen = set()
    blocks = []
    for match in results:
        content = match["metadata"]["original_content"]
        if content in seen:
            continue
        seen.add(content)
        blocks.append(content)
    return blocks


def render_rag_blocks(blocks: list[str]) -> str:
    return "\n".join(f"--- Context Segment ---\n{block}\n" for block in blocks)


def call_claude(messages, prompt, task=None, rag_context=None, output_schema=None):
    msgs = list(messages)

    system = [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}]
    if task:
        system.append({"type": "text", "text": f"\n\n<task>\n{task}\n</task>"})
    if rag_context:
        system.append({"type": "text", "text": f"\n\n<verified_context>\n{rag_context}\n</verified_context>"})

    # Only evaluator calls pass output_schema today — questioner/summarizer
    # calls leave it unset and get the same free-text behavior as before.
    kwargs = {}
    if output_schema:
        kwargs["output_config"] = {"format": {"type": "json_schema", "schema": output_schema}}

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=4096,
        system=system,
        messages=msgs,
        **kwargs,
    )
    if response.stop_reason == "max_tokens":
        raise RuntimeError(
            "Claude response was truncated (hit max_tokens) before finishing — "
            "increase max_tokens in call_claude."
        )
    return next(block.text for block in response.content if block.type == "text")


# Enforced by output_config.format on the evaluator call (see call_claude) —
# these are the only values Claude can return for each field, so there's no
# more regex parsing of free-text markdown headings.
CLUSTERS = [
    "Cluster_1_Understand_data=model+error",
    "Cluster_2_Fit_models",
    "Cluster_3_Assess_model_fit",
]

SUBCONCEPTS = [
    "1.1", "1.2", "1.3",
    "2.1", "2.2",
    "3.1", "3.2",
]

EVALUATOR_SCHEMA = {
    "type": "object",
    "properties": {
        "cluster": {"type": "string", "enum": CLUSTERS},
        "subconcept": {"type": "string", "enum": SUBCONCEPTS},
        "clarity": {"type": "string", "enum": ["High", "Low", "Irrelevant", "Incomplete"]},
        "clarity_explanation": {"type": "string"},
        "concept_understanding": {"type": "string", "enum": ["High", "Partial", "Low"]},
        "concept_understanding_explanation": {"type": "string"},
        "reasoning_quality": {"type": "string", "enum": ["High", "Medium", "Low", "Irrelevant"]},
        "reasoning_quality_explanation": {"type": "string"},
        "transfer_explanation": {"type": "string"},
    },
    "required": [
        "cluster", "subconcept",
        "clarity", "clarity_explanation",
        "concept_understanding", "concept_understanding_explanation",
        "reasoning_quality", "reasoning_quality_explanation",
        "transfer_explanation",
    ],
    "additionalProperties": False,
}


def format_evaluation(parsed: dict) -> str:
    # Re-render the evaluator's structured output as the markdown shape the
    # questioner's own few-shot examples expect (see questioner_prompt.txt).
    # Cluster/Subconcept are here so the questioner can read, from its own
    # conversation history, which clusters/subconcepts have already been
    # probed and at what level — that's the whole coverage-tracking channel,
    # no separate state machine needed.
    return (
        f"### Cluster\n{parsed['cluster']}\n"
        f"### Subconcept\n{parsed['subconcept']}\n"
        f"### Clarity\n{parsed['clarity']} - {parsed['clarity_explanation']}\n"
        f"### Concept Understanding\n{parsed['concept_understanding']} - {parsed['concept_understanding_explanation']}\n"
        f"### Reasoning Quality\n{parsed['reasoning_quality']} - {parsed['reasoning_quality_explanation']}\n"
        f"### Transfer\n{parsed['transfer_explanation']}"
    )


@app.get("/")
@app.get("/health")
def health():
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )

@app.get("/summary")
def get_summary():
    session_id = request.args.get("session_id", "")
    if session_id not in sessions:
        return jsonify(error="session_not_found"), 404
    summary = sessions[session_id].get("evaluation_summary", "No summary yet.")
    return jsonify(evaluation_summary=summary)

@app.post("/new_chat")
def new_chat():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "messages": list(BASE_MESSAGES),
        "turns": 0,
        "current_question": INITIAL_MESSAGE,
        "rag_contexts": [],
        "rubric_scores": [],
        "progress": [0, 0, 0],  # [concept, clarity, reason] counters, see get_string()
    }
    save_sessions()
    return jsonify(session_id=session_id, initial_message=INITIAL_MESSAGE)


@app.post("/string")
def get_string():
    body = request.get_json() or {}
    session_id = body.get("session_id", "")
    user_input = body.get("input", "")

    if session_id not in sessions:
        return jsonify(error="session_not_found"), 404

    session = sessions[session_id]
    current_question = session["current_question"]

    rag_blocks = get_rag_context(user_input)
    session["rag_contexts"].append(rag_blocks)
    rag_context = render_rag_blocks(rag_blocks)

    eval_messages = [
        {"role": "assistant", "content": "## Question: " + current_question},
        {"role": "user", "content": "## Answer: " + user_input},
    ]
    claude_evaluation = call_claude(
        eval_messages, evaluator_prompt, rag_context=rag_context, output_schema=EVALUATOR_SCHEMA
    )
    parsed_evaluation = json.loads(claude_evaluation)
    session.setdefault("rubric_scores", []).append({
        "cluster": parsed_evaluation["cluster"],
        "subconcept": parsed_evaluation["subconcept"],
        "clarity": parsed_evaluation["clarity"],
        "concept_understanding": parsed_evaluation["concept_understanding"],
        "reasoning_quality": parsed_evaluation["reasoning_quality"],
    })

    session["messages"].append({
        "role": "user",
        "content": "## User Input\n" + user_input + "\n## Input Assessment\n" + format_evaluation(parsed_evaluation),
    })

    task = ""

    # [concept, clarity, reason] counters carried over from the previous turn —
    # loaded from the session so progress toward a transition survives across
    # requests instead of resetting to 0 every time.
    concept, clarity, reason = session.get("progress", [0, 0, 0])

    # Transitioning to a new subconcept/cluster means the RAG lookup below
    # (grounded in the student's answer to the OLD subconcept) is about to
    # become irrelevant at best, misleading at worst, for the question the
    # questioner is about to ask. <clusters> already carries the target
    # subconcept's description, so drop the stale context here rather than
    # pass it to the questioner call.
    transitioning = concept == 2 or clarity == 2 or reason == 2

    if concept == 2 or clarity == 2 or reason == 2:
        task += (
            "- The student has just been tested on subconcept " + parsed_evaluation["subconcept"]
            + " within " + parsed_evaluation["cluster"] + ". Naturally transition to a different,"
            + " not-yet-covered subconcept in that cluster, or to a new cluster entirely, using"
            + " <clusters> and the ### Cluster / ### Subconcept tags already in the conversation"
            + " to see what has been covered."
        )
        concept = clarity = reason = 0
    elif session["rubric_scores"][-1].get("clarity") == "Incomplete":
        task = "- Mention to the student you think their response is incomplete and give them chance to correct it.\n- Restate the previous question exactly as it was asked.\n- Do not treat this as a clarity, concept, or reasoning issue."
        concept = clarity = reason = 0
    elif session["rubric_scores"][-1].get("clarity") == "Low":
        task += "- Rephrase the question by indicating the element that needs clarification.\n- Target the ambiguity of the user's input."
        clarity += 1
    elif session["rubric_scores"][-1].get("clarity") == "Irrelevant":
        task += "- Rephrase the question using different, familiar examples."
        clarity += 1
    elif session["rubric_scores"][-1].get("concept_understanding") == "Low":
        task += "- Rephrase the previous question with simpler, more familiar terms.\n- Probe for any confusion of concepts\n- Do not prompt the right answer."
        concept += 1
        clarity = 0
    elif session["rubric_scores"][-1].get("reasoning_quality") == "Low":
        task += "- Ask student to explain their reasoning with a question that probes their faulty logic.\n-Do not prompt the right answer."
        reason += 1
        clarity = 0
    elif session["rubric_scores"][-1].get("concept_understanding") == "High":
        if session["rubric_scores"][-1].get("reasoning_quality") == "High":
            concept = 2
            clarity = 0
            task += "- ask a far context knowledge transfer question using <ask_knowledge_transfer_questions>."
        elif session["rubric_scores"][-1].get("reasoning_quality") == "Medium":
            concept = 2
            clarity = 0
            task += "- ask a nearer principle transfer question surrounding the concept using <ask_knowledge_transfer_questions>."
        else:
            task += "- ask a nearer transfer question surrounding the concept using <ask_knowledge_transfer_questions>."
    elif session["rubric_scores"][-1].get("concept_understanding") == "Partial":
        concept = 2
        clarity = 0
        task += "- ask a nearer principle transfer question surrounding the concept using <ask_knowledge_transfer_questions>."
    else:
        task += "- ask a nearer, principle transfer question using <ask_knowledge_transfer_questions>."

    session["progress"] = [concept, clarity, reason]

    print(task)

    next_question = call_claude(session["messages"], questioner_prompt, task=task, rag_context=None if transitioning else rag_context,)

    session["messages"].append({"role": "assistant", "content": next_question})
    session["current_question"] = next_question
    session["turns"] += 1
    print(session["turns"])

    claude_summary = None

    if session["turns"] == 10:
        # Pool every turn's retrieved blocks and dedupe across the whole
        # session — consecutive turns on the same concept otherwise retrieve
        # a lot of the same chunks, and joining them raw just repeats them.
        # This is supplementary grounding only — the actual evidence the
        # summarizer grades against is session["messages"], where each turn
        # now carries its own ### Cluster / ### Subconcept tag.
        seen = set()
        unique_blocks = []
        for turn_blocks in session["rag_contexts"]:
            if isinstance(turn_blocks, str):  # legacy sessions predate this format
                turn_blocks = [turn_blocks]
            for block in turn_blocks:
                if block not in seen:
                    seen.add(block)
                    unique_blocks.append(block)
        all_rag = render_rag_blocks(unique_blocks)
        # Exclude the just-appended, not-yet-answered next question — Sonnet 5
        # rejects a request whose conversation ends on an assistant turn
        # ("assistant message prefill" 400).
        claude_summary = call_claude(session["messages"][:-1], summarizer_prompt, rag_context=all_rag)
        session["evaluation_summary"] = claude_summary

    save_sessions()

    return jsonify(server_message=next_question, evaluation_summary=claude_summary)


def require_admin():
    if not ADMIN_TOKEN:
        return jsonify(error="admin_not_configured"), 500
    token = request.headers.get("X-Admin-Token") or request.args.get("token")
    if token != ADMIN_TOKEN:
        return jsonify(error="unauthorized"), 401
    return None


@app.get("/admin/sessions")
def admin_list_sessions():
    err = require_admin()
    if err:
        return err
    return jsonify(sessions=[
        {
            "session_id": session_id,
            "turns": s.get("turns", 0),
            "current_question": s.get("current_question"),
            "has_summary": "evaluation_summary" in s,
        }
        for session_id, s in sessions.items()
    ])


@app.get("/admin/sessions/<session_id>")
def admin_get_session(session_id):
    err = require_admin()
    if err:
        return err
    if session_id not in sessions:
        return jsonify(error="session_not_found"), 404
    return jsonify(session_id=session_id, **sessions[session_id])


@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)
