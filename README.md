# Agentic Recruiter Resume Screening System

An end-to-end **agentic AI system** designed for **recruiters and hiring teams** to screen large volumes of resumes against a single job description and automatically shortlist the best-matching candidates.

The system uses **LLM agents orchestrated with LangGraph**, supports **batch resume screening**, provides **explainable match scores**, and includes an **optional RAG-based intelligence layer** for talent rediscovery.

---

## 🚀 What This System Does

**Recruiter workflow:**

1. Upload **one Job Description**
2. Upload **multiple resumes (PDF/DOCX)**
3. System:
   - Parses the JD once
   - Parses each resume
   - Matches resumes against the JD
   - Ranks candidates
4. Returns **Top-N shortlisted candidates** with:
   - Match score (0–100)
   - Matched skills
   - Missing skills
   - Final recommendation

No search queries.  
No manual data folders.  
No RAG misuse.

---

## 📌 CURRENT PROJECT STATUS

### COMPLETED
- Batch resume screening (1 JD → many resumes)
- Resume parsing agent (structured output)
- Job description parsing agent
- Resume ↔ JD matching agent with explainable scoring
- LangGraph-based batch orchestration with fault isolation
- FastAPI backend (`/api/screen`)
- Gradio recruiter UI (multi-file upload)
- Robust Pydantic schemas & validation
- Clean separation of **core logic vs intelligence (RAG)**

### 🔵 OPTIONAL / ADVANCED
- RAG-based **Talent Rediscovery**
- Historical resume search
- Skill normalization using knowledge bases

---

## ARCHITECTURE OVERVIEW

### Core Screening Flow (No RAG)

Recruiter Uploads JD + Resumes  
→ LangGraph  
→ JD Parser + Resume Parser (loop)  
→ Matcher Agent  
→ Ranking & Shortlisting  
→ Final JSON Output

### Intelligence Flow (Optional, RAG-based)

Job Description  
→ RAG Retriever  
→ Historical Resumes / Skill Knowledge Base

---

## TECH STACK

- Python
- LangChain
- LangGraph (agent orchestration)
- OpenAI / LLMs
- Pydantic
- FastAPI
- Gradio
- ChromaDB (optional RAG intelligence)

---

## PROJECT STRUCTURE

```
app/
├── core/                  # Core logic (NO RAG)
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── matcher.py
│   └── file_loader.py
│
├── graph/
│   ├── screening_graph.py     # Main LangGraph workflow
│   └── intelligence_graph.py  # Optional RAG intelligence
│
├── rag/                   # Optional retrieval layer
│
├── api/
│   ├── upload_routes.py
│   └── screening_routes.py
│
├── ui/
│   └── gradio_app.py
```

---

## HOW TO RUN

### 1 Start Backend
```bash
uvicorn app.api.main:app --reload
```

### 2 Start UI
```bash
python app/ui/gradio_app.py
```

### 3 Use the App
- Upload a **Job Description**
- Upload **multiple resumes**
- Choose **Top-N**
- Click **Screen Candidates**

---

## DESIGN DECISIONS

- **RAG is optional**, not forced  
- Core screening works without a vector database  
- LangGraph is used for **batch orchestration**, retries, and fault isolation  
- LLM outputs are normalized to enforce strict data contracts  

---

## AUTHOR

**Karan Singh**  
Applied LLM Engineer  
(Agentic AI • LangGraph • RAG • Production AI Systems)
