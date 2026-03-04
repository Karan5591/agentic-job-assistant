# Script to execute ingestion
"""This is especially useful because:
- We may re-run ingestion when new resumes are added
- We may rebuild vector DB
- We may clear and re-index
Without touching your core ingestion logic."""

from pathlib import Path
from app.rag.ingest import ingest_directory

DATA_PATHS = [
    Path("data/resumes"),
    Path("data/job_descriptions")
]
if __name__ == "__main__":
    for path in DATA_PATHS:
        ingest_directory(path)