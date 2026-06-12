# Learning Assessment Agent for Statistics
# Integrated with Anthropic API and Flask backend

import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import anthropic

load_dotenv()

app = Flask(__name__)

# Anthropic client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# File paths
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "history.json"
CONVERSATION_LOG = DATA_DIR / "conversation.json"

# PDF file path - update this to your PDF location
PDF_PATH = Path("/Users/yufanwei/Desktop/CourseKata Practice/drive-download-20260604T205031Z-3-001/data/COURSEKATA.pdf")

# Global state
file_id = None
chat_history = []
messages = []
current_round = 0
max_rounds = 10

SYSTEM_PROMPT = """
## Role:
1. You are an assistant for students in intro statistics, trying to assess their deep, conceptual understanding of the subject matter.
2. You can use the COURSEKATA.pdf as a source of information. But please use other resources to enhance your abilities when you ask questions.
3. You aim to be brief with your response.

## Goals:
1. Evaluate the student's conceptual understanding of COURSEKATA.pdf statistics concepts through conversation based assessment.
2. Identify the student's knowledge gaps and lack of conceptual understanding.
3. Gauge the student's understanding by asking questions that probe their faulty reasoning.
4. Stay grounded in the COURSEKATA.pdf.
5. Evaluate the transferability of student knowledge by asking questions that use the same concept but using different content.

## Skills:
1. Generating novel examples and situations that are not copied from the COURSEKATA.pdf.
2. Inferring conceptual understanding from student explanations using educational and cognitive science frameworks.

## Workflow:
Step 1: Use data to identify 3-5 different topics within this chapter that are prone to errors.
Assume that the concept that students are prone to misunderstanding most in this chapter of CourseKata is how to reduce error with a model.

Step 2: Opening Question
- Start with one broad conceptual question, it should be related to the identified topics in step 1. The question should:
1. Discern reasoning, not rote memorization
2. Allow multiple possible responses
3. Do not be too specific.

Step 3: Internal Understanding Assessment
- After each student response, silently evaluate:
- Reasoning ability: Good / Partial / Weak
- Confidence: High / Medium / Low
- Misconception Evidence: None / Possible / strong
- Do not reveal these evaluations to the student.

Step 4: Adaptive Follow-Up
- Use the conversation inputs and internal understanding assessment to choose the next question.

Step 5: next topic
- After thoroughly exploring one topic, move on to the next topic.

Step 6: Natural Ending
- The conversation should end when:
1. student shows strong understanding of at least 3 different topics, or
2. The total number of conversation rounds reaches 10.

Step 7: Final Assessment
- After conversation has ended, provide a brief assessment summary.

## Constraints:
1. Do not teach or give students hints to a correct answer in any form.
2. Only ask one question for each turn.
3. The length of each response is limited to 15 to 50 words.
4. Do not ask students to do calculations.
5. Questions should be open-ended and require explanation and reasoning.
"""


def upload_pdf():
    """Upload PDF file to Anthropic Files API."""
    global file_id
    try:
        if PDF_PATH.exists():
            with PDF_PATH.open("rb") as f:
                uploaded = client.beta.files.upload(
                    file=(PDF_PATH.name, f, "application/pdf")
                )
            file_id = uploaded.id
            print(f"PDF uploaded successfully: {file_id}")
            return True
    except Exception as e:
        print(f"Warning: Could not upload PDF: {e}")
        return False


def load_history():
    """Load chat history from file."""
    global chat_history, messages, current_round
    try:
        with open(HISTORY_FILE, "r") as f:
            chat_history = json.load(f)
        # Reconstruct messages for API
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "file",
                            "file_id": file_id
                        },
                        "cache_control": {"type": "ephemeral"}
                    },
                    {
                        "type": "text",
                        "text": "Start the assessment conversation. Ask only the opening question."
                    }
                ]
            }
        ]
        for entry in chat_history:
            if "text" in entry:
                messages.append({
                    "role": entry["role"],
                    "content": entry["text"]
                })
        current_round = len([e for e in chat_history if e["role"] == "assistant"])
    except FileNotFoundError:
        chat_history = []
        current_round = 0


def save_history():
    """Save chat history to file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)


def save_conversation_log(role, text, timestamp=None):
    """Append conversation to the master log file."""
    if timestamp is None:
        timestamp = datetime.now().isoformat()

    try:
        if CONVERSATION_LOG.exists():
            with open(CONVERSATION_LOG, "r") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append({
            "timestamp": timestamp,
            "role": role,
            "text": text
        })

        with open(CONVERSATION_LOG, "w") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving conversation log: {e}")


def ask_claude():
    """Call Claude API for assessment."""
    try:
        response = client.beta.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            betas=["files-api-2025-04-14"],
            messages=messages
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"


def start_conversation():
    """Start a new assessment conversation."""
    global current_round

    if len(messages) > 1:
        for m in reversed(messages):
            if m["role"] == "assistant":
                return m["content"]
        return ""

    assistant_text = ask_claude()
    current_round = 1
    messages.append({
        "role": "assistant",
        "content": assistant_text
    })

    chat_history.append({"role": "assistant", "text": assistant_text})
    save_history()
    save_conversation_log("assistant", assistant_text)

    return assistant_text


def continue_conversation(student_answer):
    """Continue assessment conversation with student response."""
    global current_round

    if current_round == 0:
        return start_conversation()

    if current_round >= max_rounds:
        return "The assessment conversation is complete. Thank you for participating!"

    if current_round < max_rounds:
        instruction = (
            "Silently assess the student's understanding according to the workflow. "
            "If the student has shown strong understanding of at least 3 different topics, "
            "provide the final assessment summary. Otherwise, respond naturally in 15 to 50 words "
            "and ask only one adaptive follow-up question."
        )
    else:
        instruction = (
            "This is the final round. Provide the final assessment summary. "
            "Briefly summarize demonstrated understanding, remaining gaps, and observed misconceptions."
        )

    user_content = student_answer + "\n\n" + instruction

    messages.append({
        "role": "user",
        "content": user_content
    })

    chat_history.append({"role": "user", "text": student_answer})
    save_history()
    save_conversation_log("user", student_answer)

    assistant_text = ask_claude()

    messages.append({
        "role": "assistant",
        "content": assistant_text
    })

    chat_history.append({"role": "assistant", "text": assistant_text})
    save_history()
    save_conversation_log("assistant", assistant_text)

    current_round += 1
    return assistant_text


# CORS support
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = Flask.response_class()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


# Routes
@app.get("/")
@app.get("/health")
def health():
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )


@app.post("/api/start")
def api_start():
    """Initialize and start the assessment conversation."""
    reply = start_conversation()
    return jsonify({"reply": reply})


@app.post("/api/chat")
def api_chat():
    """Continue conversation with student answer."""
    data = request.get_json() or {}
    student_answer = data.get("answer", "").strip()

    if not student_answer:
        return jsonify({"reply": "Please provide an answer."}), 400

    reply = continue_conversation(student_answer)
    return jsonify({"reply": reply})


@app.post("/api/history")
def api_history():
    """Get current chat history."""
    return jsonify({"history": chat_history})


@app.post("/api/clear")
def api_clear():
    """Clear conversation and start fresh."""
    global messages, chat_history, current_round

    chat_history.clear()
    messages.clear()
    current_round = 0

    if file_id:
        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {"type": "file", "file_id": file_id},
                    "cache_control": {"type": "ephemeral"}
                },
                {"type": "text", "text": "Start the assessment conversation. Ask only the opening question."}
            ]
        })

    save_history()
    return jsonify({"status": "cleared"})


@app.get("/api/conversation-log")
def api_conversation_log():
    """Get the master conversation log (for admin/analytics)."""
    try:
        if CONVERSATION_LOG.exists():
            with open(CONVERSATION_LOG, "r") as f:
                logs = json.load(f)
            return jsonify({"logs": logs})
        return jsonify({"logs": []})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    # Upload PDF on startup
    upload_pdf()

    # Load existing history if available
    if file_id:
        load_history()

    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port, debug=True)
