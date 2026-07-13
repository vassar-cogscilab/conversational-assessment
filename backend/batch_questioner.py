import anthropic, csv, html, re, sys, time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent / "local.env")

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "questioner_prompt.txt", encoding="utf-8") as f:
    questioner_prompt = f.read()

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
with open(BASE_DIR / "student_data.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
rag_contexts = [get_rag_context(row["response"]) for row in rows]
print(f"RAG done for {len(rows)} rows")

def system(prompt):
    return [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral", "ttl": "1h"}}]

def poll(batch_id, label):
    while True:
        b = client.messages.batches.retrieve(batch_id)
        print(f"[{label}] processing={b.request_counts.processing} succeeded={b.request_counts.succeeded}")
        if b.processing_status == "ended":
            return
        time.sleep(60)

def collect(batch_id):
    texts, cache_read, cache_write, input_tokens = {}, 0, 0, 0
    failed = []
    for r in client.messages.batches.results(batch_id):
        if r.result.type != "succeeded":
            failed.append((r.custom_id, r.result.type, getattr(r.result, "error", None)))
            continue
        texts[r.custom_id] = r.result.message.content[0].text
        usage = r.result.message.usage
        cache_read += usage.cache_read_input_tokens or 0
        cache_write += usage.cache_creation_input_tokens or 0
        input_tokens += usage.input_tokens
    print(f"cache_read={cache_read} cache_write={cache_write} uncached_input={input_tokens}")
    if failed:
        print(f"{len(failed)} rows did not succeed:")
        for custom_id, result_type, error in failed:
            print(f"  {custom_id}: {result_type} {error}")
    return texts

# Batch: single agent handles evaluation and next question together
q_batch = client.messages.batches.create(requests=[
    {
        "custom_id": f"row-{i}",
        "params": {
            "model": "claude-sonnet-5",
            "max_tokens": 1024,
            "system": system(questioner_prompt),
            "messages": [
                {"role": "assistant", "content": clean(row["prompt"])},
                {"role": "user", "content": clean(row["response"]) + f"\n\n<verified_context>\n{rag_contexts[i]}\n</verified_context>"},
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
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["follow_up_question"])
    writer.writeheader()
    for i, row in enumerate(rows):
        row["follow_up_question"] = follow_ups.get(f"row-{i}", "")
        writer.writerow(row)

print("Done. Results written to student_data.csv")
