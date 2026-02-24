from langgraph.graph import StateGraph
from app.graph.state import JobState
from app.graph.nodes import (
    resume_analyzer_node,
    job_description_node,
    matcher_node,
)


def build_job_graph():
    graph = StateGraph(JobState)

    graph.add_node("resume_analyzer", resume_analyzer_node)
    graph.add_node("job_description", job_description_node)
    graph.add_node("matcher", matcher_node)

    graph.set_entry_point("resume_analyzer")

    graph.add_edge("resume_analyzer", "job_description")
    graph.add_edge("job_description", "matcher")

    graph.set_finish_point("matcher")

    return graph.compile()