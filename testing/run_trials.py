"""
Runs simulated oral-exam conversations between the examiner bot
(backend/examiner_prompt.txt) and a student bot (one of the four
testing/claude_student_prompts personas), then reports what
understanding level the examiner concluded for each trial: High,
Poor, or Undetermined (conversation hit the turn limit without the
examiner committing to Poor or High).

Mirrors backend/app.py's call shape (model, thinking config, RAG
lookup, structured output schema, turn-limit logic) so results reflect
what the deployed examiner would actually do.

Usage:
    python run_trials.py --trials 5
    python run_trials.py --trials 3 --personas poor_brief
    python run_trials.py --trials 3 --workers 6 --out results.json
"""
import argparse
import json
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from dotenv import load_dotenv
import anthropic

TESTING_DIR = Path(__file__).resolve().parent
ROOT_DIR = TESTING_DIR.parent
BACKEND_DIR = ROOT_DIR / "backend"
CLAUDE_STUDENT_PROMPTS_DIR = TESTING_DIR / "claude_student_prompts"
CCODE_STUDENT_PROMPTS_DIR = TESTING_DIR / "ccode_student_prompts"


# API keys live in testing/.env — kept out of git by the repo-wide .env
# rule in .gitignore. Needs ANTHROPIC_API_KEY. (RAG_5-9_ollama's
# database_engine.py embeds via a local Ollama server, not a cloud API key
# — see RAG_5-9_ollama/README.md for setup.)
load_dotenv(TESTING_DIR / ".env")

# RAG_5-9_ollama, not RAG_5-9 — this trial harness embeds via a local Ollama
# server (nomic-embed-text) instead of the Voyage AI cloud API the live
# backend uses. Requires `ollama serve` running locally with that model
# pulled (`ollama pull nomic-embed-text`) — see RAG_5-9_ollama/README.md.
RAG_DIR = ROOT_DIR / "RAG_5-9_ollama"
sys.path.insert(0, str(RAG_DIR))
from database_engine import ContextualVectorDB  # noqa: E402

MODEL = "claude-sonnet-5"
MAX_TURNS = 12
INITIAL_MESSAGE = (
    "Everyone thinks of the mean as the central tendency or average, "
    "but explain what it is for the mean to be a model?"
)

PERSONAS = {
    "ccode_poor_brief": {"file": CCODE_STUDENT_PROMPTS_DIR / "poor_brief_student_ccode.txt", "expected": "Poor"},
    "ccode_poor_right": {"file": CCODE_STUDENT_PROMPTS_DIR / "poor_right_student_ccode.txt", "expected": "Poor"},
    "ccode_high_brief": {"file": CCODE_STUDENT_PROMPTS_DIR / "high_brief_student_ccode.txt", "expected": "High"},
    "ccode_high_right": {"file": CCODE_STUDENT_PROMPTS_DIR / "high_right_student_ccode.txt", "expected": "High"},
}

# Same shape as backend/app.py's EXAMINER_SCHEMA — keep in sync with it.
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
        "explanation": {"type": "string"},
        "conversation_state": {"type": "string", "enum": ["ongoing", "finished"]},
        "understanding_of_mean_as_model": {"type": "string", "enum": ["Pending", "Poor", "High"]},
        "question": {"type": "string"},
    },
    "required": [
        "target_concept", "target_misconceptions", "concept_judgment", "explanation",
        "conversation_state", "understanding_of_mean_as_model", "question",
    ],
    "additionalProperties": False,
}

# Same mapping as backend/app.py's BELIEF_TEMPLATES — keep in sync with it.
BELIEF_TEMPLATES = {
    "know": "The student demonstrates that they know concept {n}.",
    "unclear": "I cannot tell from the student's response whether they know concept {n}.",
    "do_not_know": "The student demonstrates that they do not know concept {n}.",
}


def belief_line(concept_judgment: str, judged_concept: str) -> str:
    # judged_concept is the concept of the question just answered (last
    # turn's target_concept), not this turn's parsed["target_concept"] (the
    # concept of the new question this turn is asking) — see run_trial.
    return BELIEF_TEMPLATES[concept_judgment].format(n=judged_concept)

client = anthropic.Anthropic()

rag_db = ContextualVectorDB(
    "my_contextual_db",
    db_path=str(RAG_DIR / "data" / "my_contextual_db" / "contextual_vector_db.pkl"),
)
rag_db.load_db()


def get_rag_context(query: str, k: int = 4) -> list[str]:
    try:
        results = rag_db.search(query, k=k)
    except Exception as exc:
        print(f"RAG lookup failed, continuing without context: {exc}", file=sys.stderr)
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


def call_claude(messages, prompt, rag_context=None, output_schema=None, max_tokens=4096):
    system = [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}]
    if rag_context:
        system.append({"type": "text", "text": f"\n\n<verified_context>\n{rag_context}\n</verified_context>"})

    kwargs = {}
    if output_schema:
        kwargs["output_config"] = {"format": {"type": "json_schema", "schema": output_schema}}

    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        thinking={"type": "adaptive", "display": "summarized"},
        system=system,
        messages=messages,
        **kwargs,
    )
    if response.stop_reason == "max_tokens":
        raise RuntimeError("Response was truncated (hit max_tokens)")
    return next(block.text for block in response.content if block.type == "text")


def format_examiner_turn(parsed: dict, judged_concept: str) -> str:
    lines = [f"Belief: {belief_line(parsed['concept_judgment'], judged_concept)}"]
    if parsed["conversation_state"] == "finished":
        lines.append("Conversation state: finished")
        lines.append(f"Understanding of the mean as a model: {parsed['understanding_of_mean_as_model']}")
    lines.append(f"Question: {parsed['question']}")
    return "\n".join(lines)


def run_trial(persona_name: str, student_prompt: str, examiner_prompt: str, trial_index: int) -> dict:
    examiner_messages = [{"role": "assistant", "content": INITIAL_MESSAGE}]
    student_messages = [{"role": "user", "content": INITIAL_MESSAGE}]
    current_question = INITIAL_MESSAGE
    # INITIAL_MESSAGE targets concept 1 (see backend/app.py's identical comment).
    current_target_concept = "1"
    transcript = [{"turn": 0, "role": "examiner", "text": INITIAL_MESSAGE}]
    guess = "Undetermined"
    turns_used = 0

    for turn in range(1, MAX_TURNS + 1):
        turns_used = turn

        student_rag = render_rag_blocks(get_rag_context(current_question))
        student_answer = call_claude(student_messages, student_prompt, rag_context=student_rag, max_tokens=1024)
        student_messages.append({"role": "assistant", "content": student_answer})
        transcript.append({"turn": turn, "role": "student", "text": student_answer})

        examiner_rag = render_rag_blocks(get_rag_context(student_answer))
        examiner_messages.append({"role": "user", "content": student_answer})
        raw = call_claude(examiner_messages, examiner_prompt, rag_context=examiner_rag, output_schema=EXAMINER_SCHEMA)
        parsed = json.loads(raw)
        examiner_messages.append({"role": "assistant", "content": format_examiner_turn(parsed, current_target_concept)})

        transcript.append({
            "turn": turn,
            "role": "examiner",
            "text": parsed["question"],
            "belief": belief_line(parsed["concept_judgment"], current_target_concept),
            "judged_concept": current_target_concept,
            "target_concept": parsed["target_concept"],
            "target_misconceptions": parsed["target_misconceptions"],
        })

        finished = parsed["conversation_state"] == "finished" or turn >= MAX_TURNS
        if finished:
            understanding = parsed["understanding_of_mean_as_model"]
            guess = understanding if understanding in ("Poor", "High") else "Undetermined"
            break

        current_question = parsed["question"]
        current_target_concept = parsed["target_concept"]
        student_messages.append({"role": "user", "content": current_question})

    return {
        "persona": persona_name,
        "trial_index": trial_index,
        "expected": PERSONAS[persona_name]["expected"],
        "guess": guess,
        "correct": guess == PERSONAS[persona_name]["expected"],
        "turns_used": turns_used,
        "transcript": transcript,
    }


def run_trial_safe(persona_name, student_prompt, examiner_prompt, trial_index) -> dict:
    try:
        return run_trial(persona_name, student_prompt, examiner_prompt, trial_index)
    except Exception as exc:
        traceback.print_exc()
        return {
            "persona": persona_name,
            "trial_index": trial_index,
            "expected": PERSONAS[persona_name]["expected"],
            "guess": "Error",
            "correct": False,
            "turns_used": 0,
            "error": str(exc),
            "transcript": [],
        }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=1, help="Trials to run per persona (default: 1)")
    parser.add_argument("--personas", nargs="+", choices=list(PERSONAS), default=list(PERSONAS),
                         help="Which personas to test (default: all)")
    parser.add_argument("--workers", type=int, default=3,
                         help="Concurrent trials to run at once (default: 3 — sequential; raising this sends more "
                              "concurrent requests to your local Ollama server and the Anthropic API)")
    parser.add_argument("--out", default=str(TESTING_DIR / "6_results.json"),
                         help="Path to write full results/transcripts JSON")
    args = parser.parse_args()

    with open(BACKEND_DIR / "examiner_prompt.txt", encoding="utf-8") as f:
        examiner_prompt = f.read()

    student_prompts = {name: PERSONAS[name]["file"].read_text(encoding="utf-8") for name in args.personas}
    for name, text in student_prompts.items():
        if not text.strip():
            raise SystemExit(f"{PERSONAS[name]['file']} is empty — nothing to run for persona '{name}'")

    jobs = [
        (persona_name, trial_index)
        for persona_name in args.personas
        for trial_index in range(1, args.trials + 1)
    ]

    print(f"Running {len(jobs)} trial(s) across personas {args.personas} ({args.workers} concurrent workers)...")

    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_trial_safe, persona_name, student_prompts[persona_name], examiner_prompt, trial_index): (persona_name, trial_index)
            for persona_name, trial_index in jobs
        }
        for future in as_completed(futures):
            persona_name, trial_index = futures[future]
            result = future.result()
            results.append(result)
            mark = "OK " if result["correct"] else "MISS"
            print(f"  [{mark}] {persona_name} trial {trial_index}: guess={result['guess']} "
                  f"(expected {result['expected']}, {result['turns_used']} turns)")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\nFull transcripts written to {args.out}\n")
    print(f"{'persona':<14}{'expected':<10}{'High':<6}{'Poor':<6}{'Undet.':<8}{'Error':<7}{'accuracy':<10}{'avg turns':<10}")
    for persona_name in args.personas:
        persona_results = [r for r in results if r["persona"] == persona_name]
        n = len(persona_results)
        counts = {"High": 0, "Poor": 0, "Undetermined": 0, "Error": 0}
        for r in persona_results:
            counts[r["guess"]] = counts.get(r["guess"], 0) + 1
        correct = sum(1 for r in persona_results if r["correct"])
        avg_turns = sum(r["turns_used"] for r in persona_results) / n if n else 0
        accuracy = f"{correct}/{n}"
        print(f"{persona_name:<14}{PERSONAS[persona_name]['expected']:<10}{counts['High']:<6}{counts['Poor']:<6}"
              f"{counts['Undetermined']:<8}{counts['Error']:<7}{accuracy:<10}{avg_turns:<10.1f}")


if __name__ == "__main__":
    main()
