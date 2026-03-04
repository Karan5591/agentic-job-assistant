from langchain_openai import ChatOpenAI
from app.rag.query import query_knowledge_base
from dotenv import load_dotenv
from app.agents.resume_parser import resume_parser
from app.prompts.resume_prompt import resume_prompt
from langchain_core.exceptions import OutputParserException


load_dotenv()

def analyze_resume(query: str):
    """
    Resume Analyzer Agent that can:
    - Retrieves resume content using RAG
    - Returns structured analysis
    """

    # Retrieve resume documents
    docs = query_knowledge_base(
        query=query,
        k=5)

    if not docs:
        return {"error": "No resume data found"}

    resume_context = "\n\n".join(doc["content"] for doc in docs)

    llm = ChatOpenAI(model="gpt-4o-mini")
    chain = resume_prompt | llm | resume_parser
    try:
        response = chain.invoke({"resume_text": resume_context})
        return response # Convert Pydantic model to dict
    except OutputParserException as e:
        return {"error":"Failed to parse structured resume output",
                "details": str(e)}
    except Exception as e:
        return {
            "error": "Unexpected error",
            "details": str(e),
        }

    