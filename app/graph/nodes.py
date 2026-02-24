from app.agents.resume_analyzer import analyze_resume
from app.graph.state import JobAgentState

def resume_analyzer_node(state: JobAgentState) -> JobAgentState:
    result = analyze_resume(state["resume_text"])
    state["resume_analysis"] = result
    return state

from app.agents.job_matcher import match_resume_to_job

def matcher_node(state):
    resume_dict = state["resume_analysis"].model_dump()

    result = match_resume_to_job(
        resume_data=resume_dict,
        job_description=state["job_description"]
    )

    state["match_result"] = result
    return state

def decision_node(state: JobAgentState) -> JobAgentState:
    score = state["match_result"]["match_score"]

    if score >= 80:
        state["final_decision"] = "Strong Fit, Recommend Apply"
    elif score >= 50:
        state["final_decision"] = "Moderate Fit, Upskilling Recommended"
    else:
        state["final_decision"] = "Low Fit, Not Recommended"

    return state