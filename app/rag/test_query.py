from app.rag.query import query_knowledge_base

if __name__ == "__main__":
    query = "C++ and JAVA experience required"
    results = query_knowledge_base(
        query=query,
        doc_type="job_descriptions",
        k=3
    )
    print(f"output is {results}")
    for i, r in enumerate(results, 1):
        print(f"\n--- Result {i} ---")
        print(r["content"][:300])
        print("Source:", r["source"])