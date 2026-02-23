from pathlib import Path
from app.rag.ingest import ingest_directory

DATA_PATHS = [
    Path("data/resumes"),
    Path("data/job_descriptions"),
    Path("data/market_docs"),
]

if __name__ == "__main__":
    for path in DATA_PATHS:
        ingest_directory(path)