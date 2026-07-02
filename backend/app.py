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

with open(BASE_DIR / "prompt.txt", encoding="utf-8") as f:
    system_prompt = f.read()

sys.path.insert(0, str(BASE_DIR / "RAG_5-9"))
from database_engine import ContextualVectorDB

RAG_DB_PATH = str(BASE_DIR / "RAG_5-9" / "data" / "my_contextual_db" / "contextual_vector_db.pkl")
rag_db = ContextualVectorDB("my_contextual_db", db_path=RAG_DB_PATH)
rag_db.load_db()

INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but explain what it is for the mean to be a model?"

USER_INSTRUCTION = (
    "Silently assess the student's understanding according to the workflow. "
    "If the student has shown strong understanding of at least 3 different topics, "
    "provide the final assessment summary. Otherwise, respond naturally in 15 to 50 words "
    "and ask only one adaptive follow-up question. Do not show internal assessments, "
    "round numbers, workflow details, or labels."
)

WRAP_UP = "Begin finishing this conversation"

# Conversation starter so the model sees the initial question in its history
BASE_MESSAGES = [
    {"role": "assistant", "content": INITIAL_MESSAGE},
]

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


def call_claude(messages, rag_query=None):
    dynamic_system = system_prompt
    if rag_query:
        context = get_rag_context(rag_query)
        dynamic_system += f"\n\n<verified_context>\n{context}\n</verified_context>"

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=dynamic_system,
        messages=messages,
    )
    return response.content[0].text


@app.get("/")
@app.get("/health")
def health():
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )

@app.post("/new_chat")
def new_chat():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "messages": list(BASE_MESSAGES),
        "turns": 0,
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
    turns = session["turns"]

    # Conversation over — only accept the instructor code
    if turns > 9:
        if user_input == "3030":
            instructor_prompt = (
                "An instructor of this student wants to know how much they understand this concept. "
                "Provide the final assessment summary only. Briefly summarize demonstrated understanding, "
                "remaining gaps, and observed misconceptions. Do not ask another follow-up question, "
                "do not give a numerical score, and do not provide instruction or correct answers."
            )
            all_messages = session["messages"] + [{"role": "user", "content": instructor_prompt}]
            return jsonify(server_message=call_claude(all_messages))
        else:
            return jsonify(server_message="End of conversation, please enter instructor code or start new chat")

    # Inject assessment instructions server-side so they are never exposed to the client
    instruction = USER_INSTRUCTION
    if turns > 7:
        instruction += "\n" + WRAP_UP
    if turns == 9:
        instruction = "respond to the user but then YOU MUST say goodbye"

    session["messages"].append({"role": "user", "content": user_input + "\n" + instruction})

    claude_text = call_claude(session["messages"], rag_query=user_input)

    session["messages"].append({"role": "assistant", "content": claude_text})
    session["turns"] += 1

    return jsonify(server_message=claude_text)


@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)
