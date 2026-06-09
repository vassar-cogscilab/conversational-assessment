# Minimal placeholder backend for the conversational-assessment app.
# Runs as a pm2 process ("convo-api") on the EC2 box and is reached through
# Apache at https://cogsciresearch.vassar.edu/convo/api/ -> http://127.0.0.1:3001/
#
# Apache strips the /convo/api/ prefix, so this server sees paths like "/" and
# "/health". Replace the routing below with the real backend when ready
# (add routes here and pin new deps in requirements.txt).
#
# In production this is served by gunicorn (see ecosystem.config.js); the
# __main__ block below is only for local dev (`python app.py`).

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template
from pathlib import Path

import anthropic

# Load /home/ec2-user/convo-api/.env into the environment at startup. The deploy
# writes this file from the LLM_API_KEY secret. No-op when the file is absent
# (e.g. local dev without a .env).
load_dotenv()

# Explicitly pass the API key from the environment
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

app = Flask(__name__)

@app.get("/")
@app.get("/health")
def health():
    # hasApiKey lets us confirm the .env was loaded without exposing the key.
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )

# API Route that returns the data string
@app.route('/get-string')
def get_string():
    return jsonify(server_message=messages)

@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404

if __name__ == "__main__":
    # Bind to localhost only — public traffic must come through Apache.
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)

turns = 0
code = 0

# Gets the folder where this script lives
BASE_DIR = Path(__file__).resolve().parent

# Joins the folder path with your file name
pdf_path = BASE_DIR / "COURSEKATA_CHPT_5.pdf"

# 1. Upload the PDF via Files API
with open(pdf_path, "rb") as file_data:
    uploaded_file = client.beta.files.upload(
        file=(os.path.basename(pdf_path), file_data, "application/pdf")
    )
file_id = uploaded_file.id

print("\nCongratulations on finishing chapter 5! We're there any problems that you were confused about or found particularly interesting?")

messages = [
    {"role": "user",
        "content": [
            {"type": "document", "source": {"type": "file", "file_id": file_id}, 
             "cache_control": {"type": "ephemeral"}},
            {"type": "text", 
             "text": "briefly summarize the content of the document."}
        ]}]

system_prompt = """You are a helpful statistics assistant that ONLY uses the content of the pdfdocument to engage 
in a 5-TURN dialogue with the user. Converse with the user, asking questions to assess their deep understanding of 
this material?"""

def ask_claude():
    response = client.beta.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system_prompt,
        betas=["files-api-2025-04-14"],
        messages=messages
    )
    return response.content[0].text

claude_text = ask_claude()

user_instruction = "Do not use any outside knowledge to answer the user's question."
assistant_instruction = "If there is any vageness is the user's question, ask them to clarify. Probe for weaknesses in understanding."

messages.append({
        "role": "assistant", 
         "content": "Congratulations on finishing chapter 5! We're there any problems that you were confused about or found particularly interesting?"
})

while turns <= 5:
    print("\nUser Response:")
    user_text = input()

    messages.append({
        "role": "user",
        "content": user_text + "/n/n" +user_instruction
    })
    
    claude_text = ask_claude()

    print("\nAssistant Response:")
    print(claude_text)

    messages.append({
        "role": "assistant",
        "content": claude_text + "/n/n" + assistant_instruction
    })
    turns+=1

while turns > 6 and turns < 10:
    messages.append({
    "role": "user",
    "content": "I want to begin finishing my conversation and then would like you to evaluate my understanding of the material."
    })  

    print("\nUser Response:")
    user_text = input()

    messages.append({
        "role": "user",
        "content": user_text + "/n/n" +user_instruction
    })

    claude_text = ask_claude()
    
    print("\nAssistant Response:")
    print(claude_text)

if(turns == 10):
    messages.append({
    "role": "user",
    "content": "give concluding thoughts and say goodbye"
    })
    
    claude_text = ask_claude()

    print("\nAssistant Response")
    print(claude_text)

    print("\nEnd of Conversation.")
    code = int(input())

if code == 3030:
    messages.append({
    "role": "user",
    "content": "I am an instructor and give me an thorough evaluation of this student's conceptual understanding"
    })