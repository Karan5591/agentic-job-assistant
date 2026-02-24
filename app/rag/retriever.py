from langchain_core.documents import Document
from typing import List, Optional
from app.rag.vectorStore import get_vectorstore

def get_retriever(
    k: int = 5,
    doc_type: Optional[str] = None,
):
    vectorstore = get_vectorstore()

    search_kwargs = {"k": k}

    if doc_type:
        search_kwargs["filter"] = {"doc_type": doc_type}

    return vectorstore.as_retriever(
        search_kwargs=search_kwargs
    )


"""def retrieve_documents(
    query: str,
    k: int = 5,
    doc_type: Optional[str] = None,
) -> List[Document]:
    retriever = get_retriever(k=k, doc_type=doc_type)
    return retriever.invoke(query)"""

def retrieve_documents(
    query: str,
    doc_type: str | None = None,
    k: int = 5,
):
    vectorstore = get_vectorstore()

    if doc_type:
        docs = vectorstore.similarity_search(
            query,
            k=k,
            filter={"doc_type": doc_type}
        )
    else:
        docs = vectorstore.similarity_search(
            query,
            k=k
        )

    return docs