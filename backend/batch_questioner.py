"""
Batch-tests the questioner against a CSV of student responses.

Usage:
    python batch_questioner.py --input responses.csv --output results.csv

Expected CSV columns: item_id, chapter, response, prompt, dt_submitted
Output adds a `follow_up_question` column.
"""

import argparse
import csv
import html
import re
import time
from pathlib import Path

from dotenv import load_dotenv
import anthropic

load_dotenv(dotenv_path=Path(__file__).parent / "local.env")

BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / "questioner_prompt.txt", encoding="utf-8") as f:
    QUESTIONER_PROMPT = f.read()

client = anthropic.Anthropic()


def clean_prompt(text: str) -> str:
    """Strip HTML entities and inline LaTeX wrappers for cleaner display."""
    text = html.unescape(text)
    text = re.sub(r"&[a-z]+;", " ", text)
    return text.strip()


def build_requests(rows: list[dict]) -> list[dict]:
    requests = []
    for i, row in enumerate(rows):
        question = clean_prompt(row["prompt"])
        response = row["response"].strip()
        requests.append({
            "custom_id": str(i),
            "params": {
                "model": "claude-sonnet-5",
                "max_tokens": 512,
                "system": [
                    {
                        "type": "text",
                        "text": QUESTIONER_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                "messages": [
                    {"role": "assistant", "content": question},
                    {"role": "user", "content": response},
                ],
            },
        })
    return requests


def poll_until_done(batch_id: str, interval: int = 30) -> None:
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        counts = batch.request_counts
        print(
            f"  processing={counts.processing}  "
            f"succeeded={counts.succeeded}  "
            f"errored={counts.errored}"
        )
        if batch.processing_status == "ended":
            return
        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to output CSV")
    args = parser.parse_args()

    with open(args.input, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Loaded {len(rows)} rows. Submitting batch…")
    requests = build_requests(rows)
    batch = client.messages.batches.create(requests=requests)
    print(f"Batch ID: {batch.id}")

    print("Polling for completion…")
    poll_until_done(batch.id)

    # Index results by custom_id
    results_map: dict[str, str] = {}
    for result in client.messages.batches.results(batch.id):
        if result.result.type == "succeeded":
            text = result.result.message.content[0].text
        else:
            text = f"ERROR: {result.result.type}"
        results_map[result.custom_id] = text

    fieldnames = list(rows[0].keys()) + ["follow_up_question"]
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i, row in enumerate(rows):
            row["follow_up_question"] = results_map.get(str(i), "")
            writer.writerow(row)

    print(f"Done. Results written to {args.output}")


if __name__ == "__main__":
    main()
