from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException
from pydantic import BaseModel, Field
from typing import List


class MatchResult(BaseModel):
    match_score: int = Field(..., ge=0, le=100)
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template(
    """
Compare resume and job description.

Scoring:
- Required skills: 60
- Preferred skills: 20
- Experience: 20

Return ONLY valid JSON.

Resume:
{resume}

Job Description:
{jd}

{format_instructions}
"""
)


def match_resume_to_jd(resume: dict, jd: dict) -> MatchResult:
    parser = PydanticOutputParser(pydantic_object=MatchResult)

    try:
        chain = (
            prompt.partial(
                format_instructions=parser.get_format_instructions()
            )
            | llm
            | parser
        )

        return chain.invoke({"resume": resume, "jd": jd})

    except OutputParserException as e:
        raise ValueError(
            "Failed to generate structured match result"
        ) from e

    except Exception as e:
        raise RuntimeError(
            "Unexpected error during resume-JD matching"
        ) from e