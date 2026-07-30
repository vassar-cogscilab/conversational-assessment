"""
Interactive session where YOU play the examiner and a student persona
(one of the testing/ccode_student_prompts personas) is played by Claude.

Reuses run_trials.py's setup (model, caching, RAG lookup) so the student's
behavior here matches what run_trials.py exercises automatically.

Usage:
    python chat_with_student.py
    python chat_with_student.py --persona ccode_high_brief

Type 'quit' or 'exit' to end the conversation.
"""
import argparse

from run_trials import PERSONAS, INITIAL_MESSAGE, call_claude, get_rag_context, render_rag_blocks


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--persona", choices=list(PERSONAS), default="ccode_poor_brief",
                         help="Student persona to talk to (default: ccode_poor_brief)")
    args = parser.parse_args()

    student_prompt = PERSONAS[args.persona]["file"].read_text(encoding="utf-8")
    student_messages = [{"role": "user", "content": INITIAL_MESSAGE}]

    print(f"--- Chatting with persona '{args.persona}' (type 'quit' to end) ---\n")
    print(f"You: {INITIAL_MESSAGE}\n")

    while True:
        student_rag = render_rag_blocks(get_rag_context(student_messages[-1]["content"]))
        answer = call_claude(student_messages, student_prompt, rag_context=student_rag, max_tokens=1024)
        student_messages.append({"role": "assistant", "content": answer})
        print(f"Student: {answer}\n")

        question = input("You: ").strip()
        if question.lower() in ("quit", "exit"):
            break
        student_messages.append({"role": "user", "content": question})


if __name__ == "__main__":
    main()
