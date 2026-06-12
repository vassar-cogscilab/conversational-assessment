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
from flask import Flask, jsonify, request
import anthropic
from pathlib import Path
from dotenv import load_dotenv
import json


# Load /home/ec2-user/convo-api/.env into the environment at startup. The deploy
# writes this file from the LLM_API_KEY secret. No-op when the file is absent
# (e.g. local dev without a .env).

##load_dotenv(dotenv_path="local.env")

load_dotenv()

app = Flask(__name__)

client = anthropic.Anthropic()

CHAT_HISTORY = "history.json"

try:
    with open(CHAT_HISTORY, "r", encoding="utf-8") as f:
        chat_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    chat_data = []

def save_history():
    with open(CHAT_HISTORY, "w", encoding="utf-8") as f:
        json.dump(chat_data, f, ensure_ascii=False, indent=2)

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

messages = [
    {"role": "user",
        "content": [
            {"type": "document", "source": {"type": "file", "file_id": file_id}, 
            "cache_control": {"type": "ephemeral"}},
            {"type": "text", 

            ##Remove comments to have AI formulating first question
            "text": "briefly summarize the content of the document."}##,
        ## {"type": "text",
        ##  "text": "Start the assessment conversation. Ask only the opening question."}
        ]}]

system_prompt = """
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
2. Inferring conceptual understanding from student explanations 
## using educational and cognitive science frameworks.

## Workflow:
Step 1:
## - Use data to identify 3-5 different topics within this chapter that 
## are prone to errors. 
Assume that the concept that students are prone to misunderstanding most in this chapter of CourseKata is how to reduce error with a model.

Step 2: Opening Question
- Start with one broad conceptual question, it should be related to the identified topics in step 1. The question should:
1. Discern reasoning, not rote memorization
2. Allow multiple possible responses
3. Do not be too specific.

Step 3: Internal Understanding Assessment
- After each student response, silently evaluate:
- Reasoning ability
Good / Partial / Weak
- Confidence
High / Medium / Low
- Misconception Evidence
None / Possible / strong
- Take note if the student demonstrates:

Strong understanding = good reasoning, medium to high confidence, none misconception evidence

or

Strong misunderstanding = weak reasoning, any confidence, strong misconception evidence

- Do not reveal these evaluations to the student.

Step 4: Adaptive Follow-Up
- Use the conversation inputs and internal understanding assessment to choose the next question, prioritizing as follows:
1. Good reasoning → ask a deeper application or transfer question.
2. Partial reasoning → probe the missing part of the explanation with a question.
3. Weak reasoning → probe assumptions and vague reasoning steps by asking clarifying questions.
4. The student demonstrates strong misunderstanding or strong understanding → jump to the next topic.

Step 5: next topic
- After thoroughly exploring one topic, move on to the next topic identified in step 1 and repeat steps 3-4 for that topic.

Step 6: Natural Ending
- The conversation should end when:
1. student shows strong understanding of at least 3 different topics, or
2. The total number of conversation rounds reaches 10.

Step 7: Final Assessment
- After conversation has ended, provide a brief assessment summary of the student to their instructor covering:
1. All the topics this conversation
2. Demonstrated understanding
3. Observed misconceptions
4. Possible topic that the student can explore

## Constraints:
1. Do not teach or give students hints to a correct answer in any form. 
2. Move on to the next question after assessing whether students have strong understanding or misunderstanding.
3. Only ask one question for each turn.
4. Do not tell the student they are correct or wrong during the conversation or show any tendency.
5. Formulate questions with data from outside the COURSEKATA.pdf, but that ask about similar concepts.
6. The length of each response is limited to 15 to 50 words.
8. Do not ask students to do calculations.
9. Do not ask students to give the name of the concepts or answer questions that can be easily answered with one or two words. The questions should be open-ended and require explanation and reasoning.
11. Consider language barriers, wording difficulties, and incomplete expression before inferring misunderstanding.
12. Only show the conversation content without any other information, like internal assessments, round numbers, workflow details, and titles like "Opening Questions".
13. Do not list all the topics at the beginning.
14. Do not give a numerical score unless explicitly asked in the final summary.
15. Only show the topics that are actually mentioned during the conversation in the summary, even if step 1 generates them as important topics to cover. 

## Few-Shot Examples:

### Example 1: 
"""

user_instruction = """Silently assess the student's understanding according to the workflow. If the student 
has shown strong understanding of at least 3 different topics, provide the final assessment summary. Otherwise, respond 
naturally in 15 to 50 words and ask only one adaptive follow-up question. Do not show internal assessments, round numbers, 
workflow details, or labels."""

wrap_up = "Begin finishing this conversation"

def call_claude():
    response = client.beta.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system_prompt,
        betas=["files-api-2025-04-14"],
        messages=messages
    )
    return response.content[0].text


def ask_claude():
    claude_text = call_claude()

    print("\nAssistant Response:")
    print(claude_text)

    chat_data.append({"role": "assistant", "text": claude_text})
    save_history()

    messages.append({
        "role": "assistant",
        "content": claude_text
    })
    return claude_text

def ask_user(input):
    user_text = input

    chat_data.append({"role": "user", "text": user_text})
    save_history()

    messages.append({
        "role": "user",
        "content": user_text + "\n\n" + user_instruction
    })
## call_claude()

first_message = "Everyone thinks of the mean as the central tendency or average, but what explain what it is for the mean to be a model."

messages.append({
        "role": "assistant", 
        "content": first_message
})

chat_data.append({
        "role": "assistant", 
        "text": first_message
})
save_history()


@app.get("/")
@app.get("/health")
def health():
    # hasApiKey lets us confirm the .env was loaded without exposing the key.
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )

@app.get("/chat_history")
def get_chat():
    return jsonify(chat_data)

turns = 0
code = 0

if(turns == 0):
    chat_data.append("\nNEW CONVERSATION")
    save_history

# API Route that returns the data string
@app.route('/string', methods=['GET', 'POST'])
def get_string():

    user_instruction = """Silently assess the student's understanding according to the workflow. If the student 
    has shown strong understanding of at least 3 different topics, provide the final assessment summary. Otherwise, respond 
    naturally in 15 to 50 words and ask only one adaptive follow-up question. Do not show internal assessments, round numbers, 
    workflow details, or labels."""

    wrap_up = "Begin finishing this conversation"

    user_data = request.get_json()
    user_input = user_data.get('input', '')
    turns = user_data.get('turns', 0)
    claude_text = ""

    code = 0

    if turns <= 7:
        print(turns)
        ask_user(user_input)

        claude_text = ask_claude()

    if turns > 7 and turns < 10:
        print(turns)
        user_instruction = user_instruction + "/n/n" + wrap_up

        ask_user(user_input)

        claude_text = ask_claude()

    if(turns == 10):
        print(turns)
        user_instruction = "answer my question but then YOU MUST give concluding thoughts and say goodbye"
        
        ask_user(user_input)

        claude_text = ask_claude()

        code = user_input

    if(turns > 10):
        claude_text = "End of conversation, please enter instructor code or start new chat"

        code = (user_input)

    if code == "3030":
        messages.append({
        "role": "user",
        "content": """An instructor of this student wants to know how much they understand of this concept. Provide the 
        final assessment summary only. Briefly summarize demonstrated understanding, remaining gaps, and observed misconceptions. 
        Do not ask another follow-up question, do not give a numerical score, and do not provide instruction or correct answers."""
        })

        claude_text = ask_claude()

    return jsonify(
        server_message= claude_text)# Send it back to confirm it worked!

@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    # Bind to localhost only — public traffic must come through Apache.
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)
