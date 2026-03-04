from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from pathlib import Path
import shutil
import uuid

from app.core.file_loader import load_text_from_file, load_multiple_files

router = APIRouter()

TEMP_DIR = Path("temp_uploads")
TEMP_DIR.mkdir(exist_ok=True)

@router.post("/upload")
async def upload_files(
    job_description: UploadFile = File(...),
    resumes: List[UploadFile] = File(...)
):
    """
    Upload JD + multiple resumes and extract text.
    """

    try:
        # Save JD
        jd_path = TEMP_DIR / f"{uuid.uuid4()}_{job_description.filename}"
        with open(jd_path, "wb") as f:
            shutil.copyfileobj(job_description.file, f)

        jd_text = load_text_from_file(jd_path)

        # Save resumes
        resume_paths = []
        for resume in resumes:
            path = TEMP_DIR / f"{uuid.uuid4()}_{resume.filename}"
            with open(path, "wb") as f:
                shutil.copyfileobj(resume.file, f)
            resume_paths.append(path)

        resume_texts = load_multiple_files(resume_paths)

        return {
            "job_description_text": jd_text[:1000],  # preview
            "total_resumes": len(resume_texts),
            "status": "Files uploaded and text extracted successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))