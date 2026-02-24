from pydantic import BaseModel
from typing import List


class EvaluationRequest(BaseModel):
    resume_query: str
    job_query: str


class EvaluationResponse(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    experience_alignment: str
    final_recommendation: str