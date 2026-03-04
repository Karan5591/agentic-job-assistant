from pathlib import Path
from typing import List
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    UnstructuredFileLoader,
)

SUPPORTED_LOADERS = {
    ".pdf": PyPDFLoader,
    ".docx": Docx2txtLoader,
}

def load_text_from_file(file_path: Path) -> str:
    """
    Extract raw text from a resume or job description file.
    """
    ext = file_path.suffix.lower()
    loader_cls = SUPPORTED_LOADERS.get(ext, UnstructuredFileLoader)

    loader = loader_cls(str(file_path))
    docs = loader.load()

    if not docs:
        raise ValueError(f"No text extracted from {file_path.name}")

    return "\n\n".join(doc.page_content for doc in docs)


def load_multiple_files(file_paths: List[Path]) -> List[str]:
    """
    Load and extract text from multiple resume files.
    """
    texts = []
    for path in file_paths:
        text = load_text_from_file(path)
        texts.append(text)
    return texts