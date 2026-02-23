from langchain_chroma import Chroma 
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from pathlib import Path

VECTOR_DB_PATH = Path("data/vectorstore")

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def get_vectorstore(persist: bool = True):
    embeddings = get_embeddings()

    return Chroma(
        embedding_function=embeddings,
        persist_directory=str(VECTOR_DB_PATH) if persist else None
    )