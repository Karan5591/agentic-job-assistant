from typing import TypedDict, Optional

class JobAgentState(TypedDict):
    resume_text: str
    job_description: str

    resume_analysis: Optional[dict]
    match_result: Optional[dict]

    final_decision: Optional[str]