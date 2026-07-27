import os
import re
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
RAG_DIR = BASE_DIR.parent / "RAG_5-9"

with open(BASE_DIR / "examiner_prompt.txt", encoding="utf-8") as f:
    examiner_prompt = f.read()

sys.path.insert(0, str(RAG_DIR))
from database_engine import ContextualVectorDB

RAG_DB_PATH = str(RAG_DIR / "data" / "my_contextual_db" / "contextual_vector_db.pkl")
rag_db = ContextualVectorDB("my_contextual_db", db_path=RAG_DB_PATH)
rag_db.load_db()

ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")

# Session store: session_id -> {messages, turns, current_question, rag_contexts, turn_log, evaluation_summary}.
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

BASE_MESSAGES = [
    {"role": "assistant", "content": INITIAL_MESSAGE},
]


def get_rag_context(query: str, k: int = 4) -> list[str]:
    try:
        results = rag_db.search(query, k=k)
    except Exception as exc:
        print(f"RAG lookup failed, continuing without context: {exc}")
        return []
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


def call_claude(messages, prompt, rag_context=None, output_schema=None):
    msgs = list(messages)

    system = [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}]
    if rag_context:
        system.append({"type": "text", "text": f"\n\n<verified_context>\n{rag_context}\n</verified_context>"})

    kwargs = {}
    if output_schema:
        kwargs["output_config"] = {"format": {"type": "json_schema", "schema": output_schema}}

    # display: "summarized" is required to get readable text back on Sonnet 5 —
    # thinking runs adaptively either way, but the .thinking field is empty
    # under the default "omitted" display. This is the source of truth for
    # the examiner's admin-visible reasoning trail (see turn_log in /string),
    # rather than asking the model to restate its reasoning in a schema field.
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=4096,
        thinking={"type": "adaptive", "display": "summarized"},
        system=system,
        messages=msgs,
        **kwargs,
    )
    if response.stop_reason == "max_tokens":
        raise RuntimeError(
            "Claude response was truncated (hit max_tokens) before finishing — "
            "increase max_tokens in call_claude."
        )
    text = next(block.text for block in response.content if block.type == "text")
    thinking = next((block.thinking for block in response.content if block.type == "thinking"), "")
    return text, thinking

_STRAY_UNICODE_ESCAPE_RE = re.compile(r"\\u([0-9a-fA-F]{4})")


def fix_stray_unicode_escapes(text: str) -> str:
    return _STRAY_UNICODE_ESCAPE_RE.sub(lambda m: chr(int(m.group(1), 16)), text)


MAX_TURNS = 12

EXAMINER_SCHEMA = {
    "type": "object",
    "properties": {
        "target_concept": {
            "type": "string", "enum": ["1", "2", "3", "4"],
        },
        "target_misconceptions": {"type": "array", "items": {"type": "string"}},
        "concept_judgment": {
            "type": "string", "enum": ["know", "unclear", "do_not_know"],
        },
        "conversation_state": {"type": "string", "enum": ["ongoing", "finished"]},
        "understanding_of_mean_as_model": {"type": "string", "enum": ["Pending", "Poor", "High"]},
        "question": {"type": "string"},
    },
    "required": [
        "target_concept", "target_misconceptions", "concept_judgment",
        "conversation_state", "understanding_of_mean_as_model", "question",
    ],
    "additionalProperties": False,
}

BELIEF_TEMPLATES = {
    "know": "The student demonstrates that they know concept {n}.",
    "unclear": "I cannot tell from the student's response whether they know concept {n}.",
    "do_not_know": "The student demonstrates that they do not know concept {n}.",
}


def belief_line(concept_judgment: str, judged_concept: str) -> str:

    return BELIEF_TEMPLATES[concept_judgment].format(n=judged_concept)


def format_examiner_turn(parsed: dict, judged_concept: str) -> str:
    lines = [f"Belief: {belief_line(parsed['concept_judgment'], judged_concept)}"]
    if parsed["conversation_state"] == "finished":
        lines.append("Conversation state: finished")
        lines.append(f"Understanding of the mean as a model: {parsed['understanding_of_mean_as_model']}")
    lines.append(f"Question: {parsed['question']}")
    return "\n".join(lines)


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
        "current_target_concept": "1",
        "rag_contexts": [],
        "turn_log": [],
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

    judged_concept = session.get("current_target_concept", "1")

    rag_blocks = get_rag_context(user_input)
    session["rag_contexts"].append(rag_blocks)
    rag_context = render_rag_blocks(rag_blocks)

    session["messages"].append({"role": "user", "content": user_input})

    claude_response, thinking = call_claude(
        session["messages"], examiner_prompt, rag_context=rag_context, output_schema=EXAMINER_SCHEMA
    )
    parsed = json.loads(claude_response)
    parsed["question"] = fix_stray_unicode_escapes(parsed["question"])

    session.setdefault("turn_log", []).append({
        "reasoning": thinking,
        "belief": belief_line(parsed["concept_judgment"], judged_concept),
        "judged_concept": judged_concept,
        **{k: parsed[k] for k in ("target_concept", "target_misconceptions", "concept_judgment",)},
    })

    session["messages"].append({"role": "assistant", "content": format_examiner_turn(parsed, judged_concept)})
    session["current_question"] = parsed["question"]
    session["current_target_concept"] = parsed["target_concept"]
    session["turns"] += 1

    finished = parsed["conversation_state"] == "finished" or session["turns"] >= MAX_TURNS

    if finished and "evaluation_summary" not in session:
        understanding = parsed["understanding_of_mean_as_model"]
        session["evaluation_summary"] = (
            understanding if understanding in ("Poor", "High")
            else "Understanding not determined — conversation ended at the turn limit."
        )

    save_sessions()

    return jsonify(server_message=parsed["question"], evaluation_summary=session.get("evaluation_summary"))


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
