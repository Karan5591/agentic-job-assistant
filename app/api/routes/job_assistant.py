from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.job_assistant import run_job_assistant

router = APIRouter()

class JobAssistantRequest(BaseModel):
    resume_query: str
    job_query: str

@router.post("/analyze")
def analyze_job(req: JobAssistantRequest):
    result = run_job_assistant(
        resume_query=req.resume_query,
        job_query=req.job_query
    )
    return result