from langchain_core.prompts import ChatPromptTemplate
from app.agents.resume_parser import resume_parser

resume_prompt = ChatPromptTemplate.from_template("""
- You are a resume analysis assistant.
- Extract structured information from the resume text below.
Resume:
{resume_text}
{format_instructions}""",
    partial_variables={
        "format_instructions": resume_parser.get_format_instructions()
    }
)