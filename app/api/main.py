from fastapi import FastAPI
from app.api.routes.job_assistant import router as job_router

app = FastAPI(
    title="Agentic Job Assistant API",
    version="1.0.0"
)

app.include_router(job_router, prefix="/api")