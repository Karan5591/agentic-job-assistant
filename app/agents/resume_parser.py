from langchain_core.output_parsers import PydanticOutputParser
from app.schemas.resume_schema import ResumeStructured

resume_parser = PydanticOutputParser(
    pydantic_object=ResumeStructured
)