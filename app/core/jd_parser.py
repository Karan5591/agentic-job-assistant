from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.exceptions import OutputParserException
from pydantic import BaseModel, Field
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("OPENAI_API_KEY")


# Schema
class ParsedJD(BaseModel):
    job_title: Optional[str]
    required_skills: List[str]
    preferred_skills: List[str]
    experience_level: Optional[str]

# LLM + Parser

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

parser = PydanticOutputParser(pydantic_object=ParsedJD)

prompt = ChatPromptTemplate.from_template(
    """
You are an expert technical recruiter.

Extract structured hiring requirements from the job description.
Clearly separate REQUIRED vs PREFERRED skills.
Return ONLY valid JSON.

Job Description:
{jd_text}

{format_instructions}
""",
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


def parse_job_description(jd_text: str) -> ParsedJD:
    """
    Parse JD text into structured hiring requirements.
    """
    try:
        chain = prompt | llm | parser
        return chain.invoke({"jd_text": jd_text})

    except OutputParserException as e:
        raise ValueError(
            "Failed to parse job description"
        ) from e

    except Exception as e:
        raise RuntimeError(
            "Unexpected error while parsing job description"
        ) from e