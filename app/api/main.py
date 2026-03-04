from fastapi import FastAPI
from app.api.upload_routes import router as upload_router
from app.api.screening_routes import router as screening_router

app = FastAPI(
    title="Recruiter Resume Screening API",
    version="2.0.0",
)

app.include_router(upload_router, prefix="/api")
app.include_router(screening_router, prefix="/api")