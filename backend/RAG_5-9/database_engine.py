import os
import json
import pickle
import threading
from typing import Any
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import anthropic
import voyageai # pip install voyageai
from dotenv import load_dotenv

# Assuming MODEL_NAME for Anthropic is defined globally elsewhere in your script
MODEL_NAME = "claude-haiku-4-5" 

load_dotenv()

class ContextualVectorDB:
    def __init__(self, name: str, anthropic_api_key=None, db_path=None):
        if anthropic_api_key is None:
            anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

        # Voyage AI embeddings (cloud API, no local model/tunnel needed)
        self.voyage_client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))
        self.embed_model = "voyage-4-large"

        self.anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.name = name
        self.embeddings = []
        self.metadata = []
        self.query_cache = {}
        self.db_path = db_path or f"./data/{name}/contextual_vector_db.pkl"
 
        self.token_counts = {"input": 0, "output": 0, "cache_read": 0, "cache_creation": 0}
        self.token_lock = threading.Lock()
 
    def situate_context(self, doc: str, chunk: str) -> tuple[str, Any]:
        DOCUMENT_CONTEXT_PROMPT = """
        <document>
        {doc_content}
        </document>
        """
 
        CHUNK_CONTEXT_PROMPT = """
        Here is the chunk we want to situate within the whole document
        <chunk>
        {chunk_content}
        </chunk>
 
        Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
        Answer only with the succinct context and nothing else.
        """
 
        response = self.anthropic_client.messages.create(
            model=MODEL_NAME,
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),
                            "cache_control": {
                                "type": "ephemeral"
                            },  # we will make use of prompt caching for the full documents
                        },
                        {
                            "type": "text",
                            "text": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
                        },
                    ],
                },
            ],
        )
        return response.content[0].text, response.usage
 
    def load_data(self, dataset: list[dict[str, Any]], parallel_threads: int = 1):
        if self.embeddings and self.metadata:
            print("Vector database is already loaded. Skipping data loading.")
            return
        if os.path.exists(self.db_path):
            print("Loading vector database from disk.")
            self.load_db()
            return
 
        texts_to_embed = []
        metadata = []
        total_chunks = sum(len(doc["chunks"]) for doc in dataset)
 
        def process_chunk(doc, chunk):
            contextualized_text, usage = self.situate_context(doc["content"], chunk["content"])
            with self.token_lock:
                self.token_counts["input"] += usage.input_tokens
                self.token_counts["output"] += usage.output_tokens
                self.token_counts["cache_read"] += usage.cache_read_input_tokens
                self.token_counts["cache_creation"] += usage.cache_creation_input_tokens
 
            return {
                "text_to_embed": f"{contextualized_text}\n\n{chunk['content']}",
                "metadata": {
                    "doc_id": doc["doc_id"],
                    "original_uuid": doc["original_uuid"],
                    "chunk_id": chunk["chunk_id"],
                    "original_index": chunk["original_index"],
                    "original_content": chunk["content"],
                    "contextualized_content": contextualized_text,
                },
            }
 
        print(f"Processing {total_chunks} chunks with {parallel_threads} threads")
        with ThreadPoolExecutor(max_workers=parallel_threads) as executor:
            futures = []
            for doc in dataset:
                for chunk in doc["chunks"]:
                    futures.append(executor.submit(process_chunk, doc, chunk))
 
            for future in tqdm(as_completed(futures), total=total_chunks, desc="Processing chunks"):
                result = future.result()
                texts_to_embed.append(result["text_to_embed"])
                metadata.append(result["metadata"])
 
        self._embed_and_store(texts_to_embed, metadata)
        self.save_db()
 
        print(
            f"Contextual Vector database loaded and saved. Total chunks processed: {len(texts_to_embed)}"
        )
        print(f"Total input tokens without caching: {self.token_counts['input']}")
        print(f"Total output tokens: {self.token_counts['output']}")
        print(f"Total input tokens written to cache: {self.token_counts['cache_creation']}")
        print(f"Total input tokens read from cache: {self.token_counts['cache_read']}")
 
        total_tokens = (
            self.token_counts["input"]
            + self.token_counts["cache_read"]
            + self.token_counts["cache_creation"]
        )
        savings_percentage = (
            (self.token_counts["cache_read"] / total_tokens) * 100 if total_tokens > 0 else 0
        )
        print(
            f"Total input token savings from prompt caching: {savings_percentage:.2f}% of all input tokens used were read from cache."
        )
        print("Tokens read from cache come at a 90 percent discount!")
 
    def _normalize(self, v):
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    def _embed_texts(self, texts: list[str], input_type: str) -> list[list[float]]:
        # Voyage caps batches at 1000 texts AND 120,000 tokens per call.
        # There's no local tokenizer here, so estimate tokens as chars/4 and
        # keep batches well under the cap to absorb estimation error.
        MAX_ITEMS = 1000
        MAX_CHARS = 350_000  # ~87.5k estimated tokens, safety margin under 120k

        embeddings = []
        batch: list[str] = []
        batch_chars = 0

        def flush():
            nonlocal batch, batch_chars
            if not batch:
                return
            result = self.voyage_client.embed(batch, model=self.embed_model, input_type=input_type)
            embeddings.extend(result.embeddings)
            batch, batch_chars = [], 0

        for text in texts:
            if batch and (len(batch) >= MAX_ITEMS or batch_chars + len(text) > MAX_CHARS):
                flush()
            batch.append(text)
            batch_chars += len(text)
        flush()

        return [self._normalize(e) for e in embeddings]

    def _get_single_embedding(self, text: str) -> list[float]:
        # Queries are embedded with input_type="query"; corpus chunks use
        # "document" via _embed_and_store — Voyage recommends distinguishing
        # the two for retrieval quality.
        return self._embed_texts([text], input_type="query")[0]

    def _embed_and_store(self, texts: list[str], data: list[dict[str, Any]]):
        self.embeddings = self._embed_texts(texts, input_type="document")
        self.metadata = data
 
    def search(self, query: str, k: int = 20) -> list[dict[str, Any]]:
        if query in self.query_cache:
            query_embedding = self.query_cache[query]
        else:
            query_embedding = self._get_single_embedding(query)
            self.query_cache[query] = query_embedding
 
        if not self.embeddings:
            raise ValueError("No data loaded in the vector database.")
 
        similarities = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(similarities)[::-1][:k]
 
        top_results = []
        for idx in top_indices:
            result = {
                "metadata": self.metadata[idx],
                "similarity": float(similarities[idx]),
            }
            top_results.append(result)
        return top_results
 
    def save_db(self):
        # Convert any numpy arrays back to list for reliable JSON serialization in query_cache
        serializable_cache = {k: list(v) if isinstance(v, np.ndarray) else v for k, v in self.query_cache.items()}
        data = {
            "embeddings": [list(e) if isinstance(e, np.ndarray) else e for e in self.embeddings],
            "metadata": self.metadata,
            "query_cache": json.dumps(serializable_cache),
        }
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "wb") as file:
            pickle.dump(data, file)
 
    def load_db(self):
        if not os.path.exists(self.db_path):
            raise ValueError(
                "Vector database file not found. Use load_data to create a new database."
            )
        with open(self.db_path, "rb") as file:
            data = pickle.load(file)
        self.embeddings = data["embeddings"]
        self.metadata = data["metadata"]
        self.query_cache = json.loads(data["query_cache"])