from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY")

class Experience(BaseModel):
    company: str
    role: str
    years: Optional[str] = None


class ParsedResume(BaseModel):
    candidate_name: str = Field(..., description="Full name of the candidate")
    summary: str
    skills: List[str]
    experience: List[Experience]

# LLM + Parser---------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=ParsedResume)

prompt = ChatPromptTemplate.from_template(
    """
You are an expert resume parsing agent.

Extract structured information from the resume text below.
Return ONLY valid JSON.

Resume Text:
{resume_text}

{format_instructions}
""",
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


def parse_resume(resume_text: str) -> ParsedResume:
    """
    Parse resume text into structured format.
    """
    try:
        chain = prompt | llm | parser
        return chain.invoke({"resume_text": resume_text})

    except OutputParserException as e:
        raise ValueError(
            "Failed to parse into structured format"
        ) from e

    except Exception as e:
        raise RuntimeError(
            "Unexpected error while parsing resume"
        ) from e