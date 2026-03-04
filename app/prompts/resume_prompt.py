from langchain_core.prompts import ChatPromptTemplate
from app.agents.resume_parser import resume_parser

resume_prompt = ChatPromptTemplate.from_template("""
- You are a resume analysis assistant that help in analysis of the resume documents.
- Your job is to extract the structured information from the resume text below.
- Return ONLY valid JSON. Do not include explanations.
Resume:
{resume_text}                                            
{format_instructions}""", partial_variables={"format_instructions": resume_parser.get_format_instructions()}
) 