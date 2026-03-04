
from app.agents.match_parser import match_parser
from langchain_core.prompts import ChatPromptTemplate

match_prompt = ChatPromptTemplate.from_template(
    """
    - You are an expert AI recruitment assistant.
    - Compare the resume and job description below and evaluate candidate fit.
    - Only list missing_skills if they are explicitly mentioned or strongly provided in the job description.

    **Scoring rules**:
    - Skill match: up to 60 points
    - Experience alignment: up to 25 points
    - Missing critical skills penalty: up to -20 points
    - Ensure final match_score is between 0 and 100.
    
    
    Resume (structured):
    {resume_data}
    Job Description:
    {job_description}
    
    **Evaluate**:
    - Skill overlap
    - Missing skills
    - Experience alignment
    - Overall fit
    {format_instructions}""",
    partial_variables={
        "format_instructions": match_parser.get_format_instructions()
    }
)