from langgraph.graph import StateGraph, END
from app.graph.state import JobAgentState
from app.graph.nodes import (
    resume_analyzer_node,
    matcher_node,
    decision_node
)

def build_job_graph():
    graph = StateGraph(JobAgentState)

    graph.add_node("resume_analyzer", resume_analyzer_node)
    graph.add_node("matcher", matcher_node)
    graph.add_node("decision", decision_node)

    graph.set_entry_point("resume_analyzer")

    graph.add_edge("resume_analyzer", "matcher")
    graph.add_edge("matcher", "decision")
    graph.add_edge("decision", END)

    return graph.compile()