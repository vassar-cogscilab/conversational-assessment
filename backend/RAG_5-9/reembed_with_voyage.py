"""One-time migration: re-embed the existing corpus with Voyage AI instead of
Ollama. Reuses the contextualization already stored in the pickle (the
expensive part -- 512 Claude Haiku calls) and only redoes the embedding step.

Run once after setting VOYAGE_API_KEY in your .env, using the project venv's
Python (not a system python3) so it sees the pinned dependencies:
    cd backend
    ./venv/bin/python RAG_5-9/reembed_with_voyage.py
"""
from pathlib import Path

from database_engine import ContextualVectorDB

DB_PATH = Path(__file__).parent / "data" / "my_contextual_db" / "contextual_vector_db.pkl"

db = ContextualVectorDB("my_contextual_db", db_path=str(DB_PATH))
db.load_db()
print(f"Loaded {len(db.metadata)} chunks with existing (Ollama) embeddings.")

texts_to_embed = [
    f"{m['contextualized_content']}\n\n{m['original_content']}"
    for m in db.metadata
]

db._embed_and_store(texts_to_embed, db.metadata)
db.save_db()

print(f"Re-embedded {len(db.embeddings)} chunks with Voyage ({db.embed_model}) and saved to {DB_PATH}.")
