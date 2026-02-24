from app.agents.resume_analyzer import analyze_resume
from app.graph.state import JobState
from app.rag.query import query_knowledge_base


def job_description_node(state):
    """
    Retrieves job description content using RAG
    """

    docs = query_knowledge_base(
        query=state["job_query"],
        doc_type="job_descriptions",
        k=5
    )

    if not docs:
        raise ValueError("No job descriptions found")

    job_text = "\n\n".join(d["content"] for d in docs)

    print("🔍 JOB DESCRIPTION CONTEXT:\n", job_text[:500])

    state["job_description"] = job_text
    return state

def resume_analyzer_node(state):
    # Retrieve resume content via RAG
    docs = query_knowledge_base(
        query=state["resume_query"],
        doc_type="resumes",
        k=5
    )

    if not docs:
        raise ValueError("No resume data found in vector store")

    resume_text = "\n\n".join(d["content"] for d in docs)
    print("🔍 JOB DESCRIPTION CONTEXT:\n", resume_text[:500])  # DEBUG
    #Analyze resume
    result = analyze_resume(resume_text)

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

def decision_node(state: JobState):
    score = state["match_result"]["match_score"]

    if score >= 80:
        state["final_decision"] = "Strong Fit, Recommend Apply"
    elif score >= 50:
        state["final_decision"] = "Moderate Fit, Upskilling Recommended"
    else:
        state["final_decision"] = "Low Fit, Not Recommended"

    return state