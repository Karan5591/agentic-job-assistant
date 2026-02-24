from typing import TypedDict, Optional

class JobState(TypedDict):
    # Inputs
    resume_query: str
    job_query: str

    # Intermediate
    resume_analysis: Optional[dict]
    job_description: Optional[str]

    # Output
    match_result: Optional[dict]