import os
import sys
import json
import uuid
import secrets
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
import anthropic

load_dotenv(dotenv_path="local.env")

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

CHAT_HISTORY = "history.json"
try:
    with open(CHAT_HISTORY, "r", encoding="utf-8") as f:
        chat_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    chat_data = []

def save_history():
    with open(CHAT_HISTORY, "w", encoding="utf-8") as f:
        json.dump(chat_data, f, ensure_ascii=False, indent=2)

INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but explain what it is for the mean to be a model?"

# Conversation starter so the model sees the initial question in its history
BASE_MESSAGES = [
    {"role": "assistant", "content": INITIAL_MESSAGE},
]

chat_data.append({
    "first_message": INITIAL_MESSAGE,
})
# In-memory session store: session_id -> {messages, turns}
# Requires a single gunicorn worker — sessions are lost on restart.
sessions = {}


def get_rag_context(query: str, k: int = 4) -> str:
    results = rag_db.search(query, k=k)
    blocks = []
    for match in results:
        meta = match["metadata"]
        blocks.append(
            f"--- Context Segment ---\n"
            f"Context: {meta['contextualized_content']}\n"
            f"Content:\n{meta['original_content']}\n"
        )
    return "\n".join(blocks)


def call_claude(messages, prompt, rag_query=None):
    if rag_query:
        context = get_rag_context(rag_query)
        prompt += f"\n\n<verified_context>\n{context}\n</verified_context>"

    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        system=prompt,
        messages=messages,
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
    }
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

    eval_messages = [
        {"role": "assistant", "content": "## Question: " + current_question},
        {"role": "user", "content": "## Answer: " + user_input},
    ]
    claude_evaluation = call_claude(eval_messages, evaluator_prompt, rag_query=user_input)
    print(f"Claude evaluation: {claude_evaluation}")

    session["messages"].append({
        "role": "user",
        "content": "## User Input\n" + user_input + "\n## Input Assessment\n" + claude_evaluation,
    })

    next_question = call_claude(session["messages"], questioner_prompt, rag_query=user_input)

    session["messages"].append({"role": "assistant", "content": "## Question\n" + next_question})
    session["current_question"] = next_question
    session["turns"] += 1
    print(session["turns"])

    chat_data.append({
        "user_input": user_input,
        "claude_evaluation": claude_evaluation,
        "current_question": next_question,
    })
    save_history()

    claude_summary = None

    if session["turns"] == 15:
        # After 15 turns, generate a summary of the conversation
        claude_summary = call_claude(session["messages"], summarizer_prompt, rag_query=user_input)
        session["evaluation_summary"] = claude_summary

    return jsonify(server_message=next_question, evaluation_summary=claude_summary)

@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)
