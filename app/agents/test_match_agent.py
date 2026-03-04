from app.rag.query import query_knowledge_base
from app.agents.resume_analyzer import analyze_resume
from app.agents.match_agent import match_resume_to_jd

if __name__ == "__main__":

    #Get resume
    resume_text = """
    - Python developer with 5 years of experience.
    - Basic knowledge in SQL, and data analysis.
    """

    resume_structured = analyze_resume(resume_text)

    #Get Job Description via RAG
    jd_docs = query_knowledge_base(
        query="Python, SQL and excel Data Analyst",
        doc_type="job_descriptions",
        k=3
    )

    if not jd_docs:
        print("No job description found")
        exit()

    job_description = "\n\n".join(d["content"] for d in jd_docs)

    #Match resume from the JD
    match_result = match_resume_to_jd(
        resume_data=resume_structured.model_dump(),
        job_description=job_description
    )
    print(match_result)