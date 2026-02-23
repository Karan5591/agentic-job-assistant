from app.rag.retriever import retrieve_documents
def query_knowledge_base(
    query: str,
    doc_type: str | None = None,
    k: int = 5,
):
    
    docs = retrieve_documents(
        query=query,
        doc_type=doc_type,
        k=k,
    )

    results = []
    for doc in docs:
        results.append(
            {
                "content": doc.page_content,
                "source": doc.metadata.get("source"),
                "doc_type": doc.metadata.get("doc_type"),
            }
        )

    return results