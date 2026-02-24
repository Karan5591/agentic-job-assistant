
Agentic Job Assistant

An end-to-end Agentic AI system that analyzes resumes and job descriptions using RAG, LangChain,
and structured LLM outputs. This project is built as a job-ready capstone following real-world
AI backend architecture patterns.

Key Features:
- Resume ingestion using RAG (PDF, DOCX)
- Resume analysis using LLMs
- Structured, validated outputs using Pydantic
- Vector-based semantic search (ChromaDB)
- Modular agent-based architecture
- Designed for future LangGraph orchestration

Architecture Overview:
Documents -> Ingestion -> Vector Store -> Retrieval (RAG) -> Resume Analysis Agent
-> Structured Pydantic Output -> Matching Agents (planned)

Project Structure:
app/
  agents/
  prompts/
  rag/
  schemas/
  tools/
  graph/
data/
  resumes_data/
  job_descriptions_data/
  vectorstore/

Implemented Phases:
- Phase 1: Document ingestion & vector search (RAG)
- Phase 2.1: Resume analysis agent
- Phase 2.2: Structured LLM output with Pydantic
- Phase 2.3: Resume ↔ Job Description matching agent
- Phase 2.4: LangGraph orchestration
- Phase 2.5: FastAPI backend (planned)

Tech Stack:
Python, LangChain, ChromaDB, OpenAI, Pydantic, FastAPI, LangGraph

Why This Project:
Focused on production-ready LLM pipelines, schema-enforced outputs,
and modular agentic design reflecting industry-grade AI engineering practices.

Author:
Karan Singh
AI / LLM Engineer
