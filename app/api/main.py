from fastapi import FastAPI, HTTPException
from app.orchestrator.job_assistant import run_job_assistant
from app.api.schemas import EvaluationRequest, EvaluationResponse
from app.core.logger import logger

app = FastAPI(
    title="Agentic Job Assistant",
    description="Resume and Job Matching using RAG + LangGraph",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}


@app.post("/evaluate", response_model=EvaluationResponse)
def evaluate_candidate(payload: EvaluationRequest):
    try:
        logger.info(
            "Evaluation started | resume_query='{}' | job_query='{}'",
            payload.resume_query,
            payload.job_query
        )

        result = run_job_assistant(
            resume_query=payload.resume_query,
            job_query=payload.job_query
        )

        logger.success("Evaluation completed | score={}", result["match_score"])
        return result

    except Exception as e:
        logger.exception("Evaluation failed")
        raise HTTPException(status_code=500, detail="Internal error")