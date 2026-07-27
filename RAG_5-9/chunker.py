import json
import uuid
from pathlib import Path
from natsort import natsorted
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

# 2. Define the splitters
headers_to_split_on = [
    ("#", "Header"),
    ("##", "Section"),
    ("###", "Subsection"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=False
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200,
    separators=["\n\n", "\n", " "]
)

def process_markdown_folder_to_json(folder_path: str, output_json_path: str = "chunked_dataset.json"):
    dataset = []
    path = Path(folder_path)
    
    if not path.exists():
        print(f"Error: The folder '{folder_path}' does not exist.")
        return []
        
    md_files = natsorted(list(path.glob("*.md")))
    print(f"Found {len(md_files)} markdown files to process.")
    
    for doc_idx, file_path in enumerate(md_files):
        print(f"Processing: {file_path.name}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
            
        # 1. Generate structural splits
        header_splits = markdown_splitter.split_text(file_content)
        
        # 2. Break down into text chunks
        file_chunks = text_splitter.split_documents(header_splits)
        
        # 3. Format chunks into the nested structure
        formatted_chunks = []
        for chunk_idx, chunk in enumerate(file_chunks):
            # Reconstruct the header breadcrumbs so Claude knows exactly where it belongs
            headers = []
            if "Header" in chunk.metadata: headers.append(f"# {chunk.metadata['Header']}")
            if "Section" in chunk.metadata: headers.append(f"## {chunk.metadata['Section']}")
            if "Subsection" in chunk.metadata: headers.append(f"### {chunk.metadata['Subsection']}")
            
            header_prefix = "\n".join(headers) + "\n" if headers else ""
            full_chunk_text = f"{header_prefix}{chunk.page_content}"

            formatted_chunks.append({
                "chunk_id": f"doc_{doc_idx:03d}_chunk_{chunk_idx:03d}",
                "original_index": chunk_idx,
                "content": full_chunk_text # Text string with headers retained for Claude & Ollama
            })
            
        # 4. Construct the complete document object
        document_entry = {
            "doc_id": f"doc_{doc_idx:03d}",
            "original_uuid": str(uuid.uuid4()), 
            "content": file_content,            # Full text stays identical for stable prompt caching
            "chunks": formatted_chunks
        }
        
        dataset.append(document_entry)
        
    # 5. Save the dataset to a JSON file
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(dataset, json_file, indent=4, ensure_ascii=False)
        
    total_chunks = sum(len(doc["chunks"]) for doc in dataset)
    print(f"\nFinished! Processed {len(dataset)} files into {total_chunks} total chunks.")
    return dataset

MARKDOWN_FOLDER_PATH = "./Chapters 5-9"
OUTPUT_JSON_FILE = "ready_for_db.json"

# 3. Run the chunker function
dataset = process_markdown_folder_to_json(
    folder_path=MARKDOWN_FOLDER_PATH, 
    output_json_path=OUTPUT_JSON_FILE
)