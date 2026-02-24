from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json

llm = ChatOpenAI(temperature=0)

def match_resume_to_job(resume_data: dict, job_description: str) -> dict:
    """
    Matches structured resume data with a job description
    and returns a scoring + recommendation JSON
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", """
You are an expert technical recruiter.
Compare resume data with job description.
Return ONLY valid JSON.

JSON schema:
{{
  "match_score": number (0-100),
  "matched_skills": [],
  "missing_skills": [],
  "experience_alignment": "",
  "final_recommendation": ""
}}
"""),
        ("human", """
Resume Data:
{resume_data}

Job Description:
{job_description}
""")
    ])

    chain = prompt | llm

    response = chain.invoke({
        "resume_data": json.dumps(resume_data),
        "job_description": job_description
    })

    return json.loads(response.content)