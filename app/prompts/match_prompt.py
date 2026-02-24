
from app.agents.match_parser import match_parser
from langchain_core.prompts import ChatPromptTemplate

match_prompt = ChatPromptTemplate.from_template(
    """
    - You are an expert AI recruitment assistant.
    - Compare the resume and job description below and evaluate candidate fit.
Resume (structured):
{resume_data}
Job Description:
{job_description}
Evaluate:
- Skill overlap
- Missing skills
- Experience alignment
- Overall fit
{format_instructions}""",
    partial_variables={
        "format_instructions": match_parser.get_format_instructions()
    }
)