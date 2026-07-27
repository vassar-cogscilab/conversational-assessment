import anthropic, csv, html, re, sys, time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "questioner_prompt.txt", encoding="utf-8") as f:
    questioner_prompt = f.read()
with open(BASE_DIR / "evaluator_prompt.txt", encoding="utf-8") as f:
    evaluator_prompt = f.read()

sys.path.insert(0, str(BASE_DIR / "RAG_5-9"))
from database_engine import ContextualVectorDB
rag_db = ContextualVectorDB("my_contextual_db", db_path=str(BASE_DIR / "RAG_5-9/data/my_contextual_db/contextual_vector_db.pkl"))
rag_db.load_db()

client = anthropic.Anthropic()

def get_rag_context(query, k=4):
    results = rag_db.search(query, k=k)
    return "\n".join(
        f"--- Context Segment ---\nContext: {m['metadata']['contextualized_content']}\nContent:\n{m['metadata']['original_content']}\n"
        for m in results
    )

def clean(text):
    return re.sub(r"&[a-z]+;", " ", html.unescape(text)).strip()

# Load rows and pre-fetch RAG
rows = list(csv.DictReader(open("student_data.csv")))
rag_contexts = [get_rag_context(row["response"]) for row in rows]
print(f"RAG done for {len(rows)} rows")

def system(prompt):
    return [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}]

def poll(batch_id, label):
    while True:
        b = client.messages.batches.retrieve(batch_id)
        print(f"[{label}] processing={b.request_counts.processing} succeeded={b.request_counts.succeeded}")
        if b.processing_status == "ended":
            return
        time.sleep(60)

def collect(batch_id):
    return {r.custom_id: r.result.message.content[0].text for r in client.messages.batches.results(batch_id) if r.result.type == "succeeded"}

# Batch 1: evaluator
eval_batch = client.messages.batches.create(requests=[
    {
        "custom_id": f"row-{i}",
        "params": {
            "model": "claude-sonnet-5",
            "max_tokens": 1024,
            "system": system(evaluator_prompt),
            "messages": [
                {"role": "assistant", "content": "## Question: " + clean(row["prompt"])},
                {"role": "user", "content": "## Answer: " + row["response"] + f"\n\n<verified_context>\n{rag_contexts[i]}\n</verified_context>"},
            ],
        }
    }
    for i, row in enumerate(rows)
])
print(f"Evaluator batch: {eval_batch.id}")
poll(eval_batch.id, "evaluator")
evaluations = collect(eval_batch.id)

# Batch 2: questioner
q_batch = client.messages.batches.create(requests=[
    {
        "custom_id": f"row-{i}",
        "params": {
            "model": "claude-sonnet-5",
            "max_tokens": 512,
            "system": system(questioner_prompt),
            "messages": [
                {"role": "assistant", "content": clean(row["prompt"])},
                {"role": "user", "content": "## User Input\n" + row["response"] + "\n## Input Assessment\n" + evaluations.get(f"row-{i}", "") + f"\n\n<verified_context>\n{rag_contexts[i]}\n</verified_context>"},
            ],
        }
    }
    for i, row in enumerate(rows)
])
print(f"Questioner batch: {q_batch.id}")
poll(q_batch.id, "questioner")
follow_ups = collect(q_batch.id)

# Write output
with open("student_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["evaluation", "follow_up_question"])
    writer.writeheader()
    for i, row in enumerate(rows):
        row["evaluation"] = evaluations.get(f"row-{i}", "")
        row["follow_up_question"] = follow_ups.get(f"row-{i}", "")
        writer.writerow(row)

print("Done. Results written to student_data.csv")
