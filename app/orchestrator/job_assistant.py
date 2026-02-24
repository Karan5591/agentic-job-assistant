from app.graph.job_graph import build_job_graph
from app.schemas.resume_schema import ResumeStructured


def run_job_assistant(resume_query: str, job_query: str):
    """
    Orchestrates the full Job Assistant flow using LangGraph
    """

    graph = build_job_graph()

    initial_state = {
        "resume_query": resume_query,
        "job_query": job_query,
        "resume_analysis": None,
        "job_description": None,
        "match_result": None,
    }

    final_state = graph.invoke(initial_state)

    return final_state["match_result"]