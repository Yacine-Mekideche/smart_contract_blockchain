from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def create_conversational_chain(vectorstore):
    """
    Crée une chaîne QA conversationnelle à partir de l'index FAISS + ChatOpenAI.
    """
    llm = ChatOpenAI(temperature=0)
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=False
    )
