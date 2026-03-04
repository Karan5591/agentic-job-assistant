from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict
class ScreeningState(TypedDict):
    
    jd_text: str
    resumes: List[Dict[str, Any]]  # [{ "text": str, "file_name": str }]
    parsed_jd: Optional[Dict[str, Any]]
    results: List[Dict[str, Any]]
    current_index: int
    top_n: int

from langgraph.graph import StateGraph, END

from app.core.resume_parser import parse_resume
from app.core.jd_parser import parse_job_description
from app.core.matcher import match_resume_to_jd

def parse_jd_node(state: ScreeningState) -> ScreeningState:
    parsed_jd = parse_job_description(state["jd_text"])

    state["parsed_jd"] = parsed_jd.model_dump()
    state["results"] = []
    state["current_index"] = 0

    return state

def process_resume_node(state: ScreeningState) -> ScreeningState:
    index = state["current_index"]
    resumes = state["resumes"]

    if index >= len(resumes):
        return state  # loop exit handled elsewhere

    resume_item = resumes[index]

    try:
        parsed_resume = parse_resume(resume_item["text"])

        match_result = match_resume_to_jd(
            resume=parsed_resume.model_dump(),
            jd=state["parsed_jd"]
        )

        state["results"].append(
            {
                "candidate_name": parsed_resume.candidate_name,
                "file_name": resume_item["file_name"],
                "match_score": match_result.match_score,
                "matched_skills": match_result.matched_skills,
                "missing_skills": match_result.missing_skills,
                "recommendation": match_result.recommendation,
            }
        )

    except Exception as e:
        
        state["results"].append(
            {
                "candidate_name": resume_item["file_name"],
                "error": str(e),
                "match_score": 0,
            }
        )

    state["current_index"] += 1
    return state

def should_continue_node(state: ScreeningState) -> str:
    if state["current_index"] < len(state["resumes"]):
        return "process_resume"
    return "rank_results"

def rank_results_node(state: ScreeningState) -> ScreeningState:
    valid_results = [
        r for r in state["results"]
        if "match_score" in r
    ]

    ranked = sorted(
        valid_results,
        key=lambda x: x["match_score"],
        reverse=True
    )

    state["results"] = ranked[: state["top_n"]]
    return state

def build_screening_graph():
    graph = StateGraph(ScreeningState)

    graph.add_node("parse_jd", parse_jd_node)
    graph.add_node("process_resume", process_resume_node)
    graph.add_node("rank_results", rank_results_node)

    graph.set_entry_point("parse_jd")

    graph.add_edge("parse_jd", "process_resume")

    graph.add_conditional_edges(
        "process_resume",
        should_continue_node,
        {
            "process_resume": "process_resume",
            "rank_results": "rank_results",
        },
    )

    graph.add_edge("rank_results", END)

    return graph.compile()