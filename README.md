Agentic Job Assistant

An end-to-end Agentic AI system that analyzes resumes, matches them against job descriptions, and provides structured, explainable recommendations using LangGraph, RAG, and LLM agents.

CURRENT PROJECT STATUS (CHECKPOINT)

COMPLETED:
- Resume ingestion using RAG (PDF/DOCX)
- Vector store powered semantic retrieval
- Resume Analyzer Agent (structured JSON output)
- Job Matcher Agent (score, skill gap, recommendation)
- LangGraph-based agent orchestration
- End-to-end pipeline tested via CLI
- Robust Pydantic schemas

IN PROGRESS:
- FastAPI backend
- Gradio-based UI
- Deployment & scaling

ARCHITECTURE OVERVIEW

User Input (Resume + JD)
        |
        v
   Orchestrator
        |
        v
     LangGraph
    /         \
Resume Agent  Job Matcher
        |
        v
   Final JSON Output

TECH STACK


- Python
- LangChain
- LangGraph
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Pydantic
- FastAPI (upcoming)
- Gradio (upcoming)

PROJECT STRUCTURE

app/
 ├── agents/          # Resume analyzer & job matcher agents
 ├── graph/           # LangGraph nodes & state
 ├── orchestrator/    # Entry point orchestration logic
 ├── rag/             # Document ingestion & retrieval
 ├── schemas/         # Pydantic schemas
 ├── prompts/         # Prompt templates
 └── tests/           # CLI test scripts

HOW TO RUN (CURRENT)

uv sync
python app/orchestrator/test_orchestrator.py

NEXT MILESTONES

- FastAPI API layer
- Gradio UI
- API + UI integration
- Deployment-ready version

AUTHOR

Karan Singh
Applied LLM Engineer (Agentic AI, RAG, LangGraph)
