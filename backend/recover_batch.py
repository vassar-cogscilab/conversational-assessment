import anthropic, csv, sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path="local.env")

BASE_DIR = Path(__file__).parent
BATCH_ID = sys.argv[1] if len(sys.argv) > 1 else "msgbatch_01XY4Vzu2wYMNaZZQfXxnBGW"

client = anthropic.Anthropic()

with open(BASE_DIR / "student_data.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

texts, failed = {}, []
for r in client.messages.batches.results(BATCH_ID):
    if r.result.type != "succeeded":
        failed.append((r.custom_id, r.result.type, getattr(r.result, "error", None)))
        continue
    texts[r.custom_id] = next((b.text for b in r.result.message.content if b.type == "text"), "")

print(f"recovered {len(texts)} / {len(rows)} rows")
if failed:
    print(f"{len(failed)} rows did not succeed:")
    for custom_id, result_type, error in failed:
        print(f"  {custom_id}: {result_type} {error}")

with open(BASE_DIR / "student_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["follow_up_question"])
    writer.writeheader()
    for i, row in enumerate(rows):
        row["follow_up_question"] = texts.get(f"row-{i}", "")
        writer.writerow(row)

print("Done. Results written to student_data.csv")
