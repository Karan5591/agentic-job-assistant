from langchain_openai import ChatOpenAI
from app.prompts.match_prompt import match_prompt
from app.agents.match_parser import match_parser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
match_chain = match_prompt | llm | match_parser
def match_resume_to_jd(resume_data: dict, job_description: str):
    return match_chain.invoke(
        {
            "resume_data": resume_data,
            "job_description": job_description
        }
    )