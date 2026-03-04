from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from app.rag.query import query_knowledge_base

class IntelligenceState(TypedDict):
    jd_query: str

    # RAG outputs
    retrieved_resumes: List[Dict[str, Any]]

def retrieve_similar_resumes_node(
    state: IntelligenceState,
) -> IntelligenceState:
    """
    Uses RAG to retrieve historically similar resumes
    """
    docs = query_knowledge_base(
        query=state["jd_query"],
        doc_type="resumes",
        k=5,
    )

    state["retrieved_resumes"] = docs
    return state

def build_intelligence_graph():
    graph = StateGraph(IntelligenceState)

    graph.add_node(
        "retrieve_similar_resumes",
        retrieve_similar_resumes_node,
    )

    graph.set_entry_point("retrieve_similar_resumes")
    graph.set_finish_point("retrieve_similar_resumes")

    return graph.compile()