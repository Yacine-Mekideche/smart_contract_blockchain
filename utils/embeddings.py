from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks):
    """
    Crée un index vectoriel FAISS à partir d'une liste de textes (chunks).
    """
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(texts=chunks, embedding=embeddings)
