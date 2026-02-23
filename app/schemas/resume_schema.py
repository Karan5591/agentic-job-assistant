from typing import List, Optional
from pydantic import BaseModel, Field


class Experience(BaseModel):
    company: str
    role: str
    years: Optional[str] = None


class ResumeStructured(BaseModel):
    summary: str = Field(..., description="Professional summary")
    skills: List[str]
    experience: List[Experience]