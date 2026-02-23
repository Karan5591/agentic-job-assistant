from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.rag.query import query_knowledge_base
import json
import os
from dotenv import load_dotenv
from app.agents.resume_parser import resume_parser
from app.prompts.resume_prompt import resume_prompt


load_dotenv()

def analyze_resume(query: str = "Analyze my resume") -> Dict[str, Any]:
    """
    Resume Analyzer Agent
    - Retrieves resume content using RAG
    - Returns structured analysis
    """

    # Retrieve resume documents
    docs = query_knowledge_base(
        query=query,
        
        k=5
    )

    if not docs:
        return {"error": "No resume data found"}

    resume_context = "\n\n".join(
        d["content"] for d in docs
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    chain = resume_prompt | llm | resume_parser
    response = chain.invoke(
        {"resume_text": resume_context})

    # Parse the JSON
    try:
        return response
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by LLM",
            "raw_output": response.content}