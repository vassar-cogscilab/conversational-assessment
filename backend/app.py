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


def get_rag_context(query: str, k: int = 4) -> str:
    # RAG embeddings run through Ollama over an SSH tunnel to a remote
    # research machine — treat that link as unreliable and degrade to no
    # context rather than 500ing the student's turn if it's down.
    try:
        results = rag_db.search(query, k=k)
    except Exception as exc:
        print(f"RAG lookup failed, continuing without context: {exc}")
        return ""
    blocks = []
    for match in results:
        meta = match["metadata"]
        blocks.append(
            f"--- Context Segment ---\n"
            f"Context: {meta['contextualized_content']}\n"
            f"Content:\n{meta['original_content']}\n"
        )
    return "\n".join(blocks)


def call_claude(messages, prompt, rag_context=None):
    msgs = list(messages)
    if rag_context:
        tag = f"\n\n<verified_context>\n{rag_context}\n</verified_context>"
        if msgs and msgs[-1]["role"] == "user":
            msgs[-1] = {**msgs[-1], "content": msgs[-1]["content"] + tag}
        else:
            msgs.append({"role": "user", "content": tag})

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        system=[{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}],
        messages=msgs,
    )
    return next(block.text for block in response.content if block.type == "text")


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

    rag_context = get_rag_context(user_input)
    session["rag_contexts"].append(rag_context)

    eval_messages = [
        {"role": "assistant", "content": "## Question: " + current_question},
        {"role": "user", "content": "## Answer: " + user_input},
    ]
    claude_evaluation = call_claude(eval_messages, evaluator_prompt, rag_context=rag_context)
    print(f"Claude evaluation: {claude_evaluation}")

    session["messages"].append({
        "role": "user",
        "content": "## User Input\n" + user_input + "\n## Input Assessment\n" + claude_evaluation,
    })

    next_question = call_claude(session["messages"], questioner_prompt, rag_context=rag_context)

    session["messages"].append({"role": "assistant", "content": next_question})
    session["current_question"] = next_question
    session["turns"] += 1
    print(session["turns"])

    claude_summary = None

    if session["turns"] == 10:
        all_rag = "\n\n".join(session["rag_contexts"])
        claude_summary = call_claude(session["messages"], summarizer_prompt, rag_context=all_rag)
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
