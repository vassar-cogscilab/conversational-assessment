import os
import json
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
import anthropic

load_dotenv(dotenv_path="local.env")

app = Flask(__name__)
client = anthropic.Anthropic()

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "prompt.txt", encoding="utf-8") as f:
    system_prompt = f.read()

pdf_path = BASE_DIR / "COURSEKATA_CHPT_5.pdf"
with open(pdf_path, "rb") as f:
    uploaded_file = client.beta.files.upload(
        file=(pdf_path.name, f, "application/pdf")
    )
file_id = uploaded_file.id

CHAT_HISTORY = "history.json"
try:
    with open(CHAT_HISTORY, "r", encoding="utf-8") as f:
        chat_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    chat_data = []

def save_history():
    with open(CHAT_HISTORY, "w", encoding="utf-8") as f:
        json.dump(chat_data, f, ensure_ascii=False, indent=2)


def call_claude(messages):
    response = client.beta.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system_prompt,
        betas=["files-api-2025-04-14"],
        messages=messages,
    )
    return response.content[0].text


# Lazily initialized on first request so startup is fast.
_base_messages = None

def get_base_messages():
    global _base_messages
    if _base_messages is None:
        msgs = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {"type": "file", "file_id": file_id},
                        "cache_control": {"type": "ephemeral"},
                    },
                    {"type": "text", "text": "briefly summarize the content of the document."},
                ],
            }
        ]
        summary = call_claude(msgs)
        msgs.append({"role": "assistant", "content": summary})
        msgs.append({
            "role": "user",
            "content": "Now move on to the assessment. Start by asking the most important question involving the concept of data models that you want to assess my understanding of.",
        })
        _base_messages = msgs
    return _base_messages


@app.get("/")
@app.get("/health")
def health():
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )


@app.get("/chat_history")
def get_chat():
    return jsonify(chat_data)


@app.route("/string", methods=["GET", "POST"])
def get_string():
    user_data = request.get_json() or {}
    user_messages = user_data.get("messages", [])
    turns = user_data.get("turns", 0)
    user_input = user_data.get("input", "")

    all_messages = get_base_messages() + user_messages

    if turns <= 9:
        claude_text = call_claude(all_messages)
    else:
        if user_input == "3030":
            all_messages = all_messages + [{
                "role": "user",
                "content": (
                    "An instructor of this student wants to know how much they understand this concept. "
                    "Provide the final assessment summary only. Briefly summarize demonstrated understanding, "
                    "remaining gaps, and observed misconceptions. Do not ask another follow-up question, "
                    "do not give a numerical score, and do not provide instruction or correct answers."
                ),
            }]
            claude_text = call_claude(all_messages)
        else:
            claude_text = "End of conversation, please enter instructor code or start new chat"

    return jsonify(server_message=claude_text)


@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)
