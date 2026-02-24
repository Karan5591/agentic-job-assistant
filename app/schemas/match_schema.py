from typing import List
from pydantic import BaseModel, Field

class ResumeJDMatch(BaseModel):
    match_score: int = Field(..., ge=0, le=100)
    matched_skills: List[str]
    missing_skills: List[str]
    experience_alignment: str
    final_recommendation: str