from app.schemas.match_schema import ResumeJDMatch
from langchain_core.output_parsers import PydanticOutputParser

match_parser = PydanticOutputParser(
    pydantic_object=ResumeJDMatch
)