import os
import json
from dotenv import load_dotenv

# Import the class engine directly from your separate file
from database_engine import ContextualVectorDB

# Configurations
load_dotenv()
MODEL_NAME = "claude-haiku-4-5"
DB_NAME = "my_contextual_db"
INPUT_JSON_PATH = "./ready_for_db.json"


def ask_claude(query: str, db: ContextualVectorDB, num_chunks: int = 5) -> str:
    """Retrieves relevant context chunks and passes them to Claude."""
    search_results = db.search(query, k=num_chunks)
    
    context_blocks = []
    for match in search_results:
        metadata = match["metadata"]
        block = (
            f"--- Context Segment (Doc: {metadata['doc_id']}) ---\n"
            f"Situational Context: {metadata['contextualized_content']}\n"
            f"Content:\n{metadata['original_content']}\n"
        )
        context_blocks.append(block)
        
    full_context = "\n".join(context_blocks)

    SYSTEM_PROMPT = """You are an expert research assistant. Answer the user's question using ONLY the verified context fragments provided below. 

Guidelines:
1. Rely strictly on the provided context fragments. Do not invent facts.
2. Use the provided 'Situational Context' to understand how each fragment links back to its parent document structure.
3. If the answer cannot be found in the fragments, state clearly that you do not know.

<verified_context>
{context}
</verified_context>"""

    response = db.anthropic_client.messages.create(
        model=MODEL_NAME,
        max_tokens=1200,
        temperature=0.2,
        system=SYSTEM_PROMPT.format(context=full_context),
        messages=[{"role": "user", "content": query}]
    )
    return response.content[0].text


if __name__ == "__main__":
    if not os.path.exists(INPUT_JSON_PATH):
        print(f"Error: Missing input file. Please verify '{INPUT_JSON_PATH}' exists.")
        exit(1)

    print(f"Loading data from: {INPUT_JSON_PATH}")
    with open(INPUT_JSON_PATH, "r", encoding="utf-8") as f:
        transformed_dataset = json.load(f)
 
    # Initialize the engine imported from database_engine.py
    contextual_db = ContextualVectorDB(DB_NAME)
 
    # Process or load from hard drive automatically
    contextual_db.load_data(transformed_dataset, parallel_threads=5)
    
    print("\n" + "="*50)
    print(" CONTEXTUAL RETRIEVAL SYSTEM ONLINE")
    print("="*50 + "\n")
    
    while True:
        try:
            user_input = input("Ask a question (or type 'exit'): ").strip()
            if user_input.lower() in ['exit', 'quit']:
                break
            if not user_input:
                continue
                
            print("\nRetrieving chunks and querying Claude...")
            answer = ask_claude(query=user_input, db=contextual_db, num_chunks=4)
            
            print(f"\nClaude:\n{answer}\n")
            print("-" * 50 + "\n")
            
        except KeyboardInterrupt:
            break