from pathlib import Path
from tqdm import tqdm
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.vectorStore import get_vectorstore
from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader ,
    UnstructuredFileLoader,
)

Supported_Extensions = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
}

def load_document(file_path: Path):
    ext = file_path.suffix.lower()
    loader_class = Supported_Extensions.get(ext, UnstructuredFileLoader)
    loader = loader_class(str(file_path))
    docs = loader.load()    
    return docs

def ingest_directory(directory: Path):
    vectorstore = get_vectorstore()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    all_chunks = []

    files = [f for f in directory.glob("**/*") if f.is_file()]
    for file in tqdm(files, desc=f"Ingesting {directory.name}"):
        try:
            docs = load_document(file)

            if not docs:
                continue

            chunks = splitter.split_documents(docs)

            # Attach metadata AFTER chunking
            for chunk in chunks:
                chunk.metadata["doc_type"] = directory.name
                chunk.metadata["file_name"] = file.name
            all_chunks.extend(chunks)

        except Exception as e:
            print(f"⚠️ Skipping {file.name}: {e}")

    if not all_chunks:
        print(f"⚠️ No chunks created for {directory}")
        return

    vectorstore.add_documents(all_chunks)
    #vectorstore.persist()

    print(f"Ingested {len(all_chunks)} chunks from {directory}")
   

    