from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from typing import List
from pathlib import Path
import shutil
import uuid
from app.core.file_loader import load_text_from_file
from app.graph.screening_graph import build_screening_graph

router = APIRouter()

TEMP_DIR = Path("temp_uploads")
TEMP_DIR.mkdir(exist_ok=True)


@router.post("/screen")
async def screen_candidates(
    job_description: UploadFile = File(...),
    resumes: List[UploadFile] = File(...),
    top_n: int = Form(5),
):
    """
    Screen multiple resumes against a single job description
    and return top-N candidates.
    """

    if not resumes:
        raise HTTPException(
            status_code=400,
            detail="At least one resume must be uploaded",
        )

    try:
        # -----------------------------
        # Save & extract JD
        # -----------------------------
        jd_path = TEMP_DIR / f"{uuid.uuid4()}_{job_description.filename}"
        with open(jd_path, "wb") as f:
            shutil.copyfileobj(job_description.file, f)

        jd_text = load_text_from_file(jd_path)

        # -----------------------------
        # Save & extract resumes
        # -----------------------------
        resume_items = []

        for resume in resumes:
            resume_path = TEMP_DIR / f"{uuid.uuid4()}_{resume.filename}"
            with open(resume_path, "wb") as f:
                shutil.copyfileobj(resume.file, f)

            resume_text = load_text_from_file(resume_path)

            resume_items.append(
                {
                    "text": resume_text,
                    "file_name": resume.filename,
                }
            )

        # -----------------------------
        # Build LangGraph
        # -----------------------------
        graph = build_screening_graph()

        initial_state = {
            "jd_text": jd_text,
            "resumes": resume_items,
            "parsed_jd": None,
            "results": [],
            "current_index": 0,
            "top_n": top_n,
        }

        final_state = graph.invoke(initial_state)

        return {
            "total_resumes": len(resumes),
            "shortlisted": len(final_state["results"]),
            "top_candidates": final_state["results"],
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Screening failed: {str(e)}",
        )