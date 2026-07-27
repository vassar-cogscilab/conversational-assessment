# RAG_5-9_ollama

A parallel, Ollama-based copy of `../RAG_5-9` — the version that predates
commit `ddd5711` ("Changed embedding model and fixed data leak"), which
switched the live backend over to Voyage AI embeddings.

**This is not what the live backend/deploy uses.** `backend/app.py` and
`testing/run_trials.py` both point at `../RAG_5-9`, which is the current,
Voyage-embedded corpus. This folder exists as a restored alternative /
reference — nothing was changed in the live path to add it.

## What's different from `../RAG_5-9`

- `database_engine.py` here uses a local Ollama client (`nomic-embed-text`,
  768-dim embeddings, defaults to `http://localhost:11434`) instead of the
  Voyage AI cloud API (`voyage-4-large`, 1024-dim).
- `data/my_contextual_db/contextual_vector_db.pkl` here holds the matching
  Ollama-embedded vectors for the same 512 chunks — **do not mix and match**
  the two `.pkl` files with the two `database_engine.py` variants; the
  embedding spaces aren't compatible and similarity search will silently
  return meaningless results if you do.
- Everything else (`chunker.py`, `lllm_rag.py`, `ready_for_db.json`,
  `Chapters 5-9/`) is byte-identical between the two folders — those aren't
  affected by the embedding model choice.

## Using it

Requires a local Ollama server running (`ollama serve`, or the desktop app)
with the embedding model pulled:

```bash
ollama pull nomic-embed-text
```

Plus the `ollama` Python package on top of what's already in
`backend/requirements.txt`:

```bash
venv/bin/pip install -r RAG_5-9_ollama/requirements-ollama.txt
```

Then point any script at this folder instead of `../RAG_5-9`, e.g.:

```python
sys.path.insert(0, str(ROOT_DIR / "RAG_5-9_ollama"))
from database_engine import ContextualVectorDB

rag_db = ContextualVectorDB(
    "my_contextual_db",
    db_path=str(ROOT_DIR / "RAG_5-9_ollama" / "data" / "my_contextual_db" / "contextual_vector_db.pkl"),
)
rag_db.load_db()
```

No local Ollama tunnel/remote-machine setup needed — `Client()` defaults to
`localhost:11434`. (The original Ollama setup this restores used an SSH
tunnel to a remote research machine; the stale comment referencing that in
`backend/app.py` predates the Voyage switch and no longer describes either
RAG folder's actual setup.)
