from app.graph.job_graph import build_job_graph

if __name__ == "__main__":
    graph = build_job_graph()

    initial_state = {
        "resume_text": "Python developer with 5 years experience in SQL and backend systems...",
        "job_description": "Looking for Python and SQL developer with 4–6 years experience"
    }

    result = graph.invoke(initial_state)

    print("\nFINAL DECISION:")
    print(result["final_decision"])