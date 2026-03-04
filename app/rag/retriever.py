from typing import Optional
from app.rag.vectorStore import get_vectorstore

def retrieve_documents(
    query: str,
    k: int = 5,
    doc_type: Optional[str] = None,
):
    vectorstore = get_vectorstore()

    search_kwargs = {"k": k}
    if doc_type:
        search_kwargs["filter"] = {"doc_type": doc_type}

    # PUBLIC + STABLE API
    return vectorstore.similarity_search_with_relevance_scores(
        query=query,
        **search_kwargs
    )


