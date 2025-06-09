from .chunking import split_solidity_code
from .embeddings import create_vectorstore
from .llm import create_conversational_chain

def summarize_code(code: str, question: str = None) -> str:

    chunks      = split_solidity_code(code)
    vectorstore = create_vectorstore(chunks)
    qa_chain    = create_conversational_chain(vectorstore)

    if question:
        return qa_chain.run(question)
    return qa_chain.run(
    "Give me a concise summary of this smart contract,"
    "briefly explaining the features and key points."
    )
