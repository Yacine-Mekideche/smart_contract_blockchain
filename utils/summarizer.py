from .chunking import split_solidity_code
from .embeddings import create_vectorstore
from .llm import create_conversational_chain

def summarize_code(code: str, question: str = None) -> str:
    """
    Si 'question' est None, renvoie un résumé global du code.
    Sinon, répond à la question posée via un QA.
    """
    chunks      = split_solidity_code(code)
    vectorstore = create_vectorstore(chunks)
    qa_chain    = create_conversational_chain(vectorstore)

    if question:
        return qa_chain.run(question)
    return qa_chain.run(
        "Donne-moi un résumé concis de ce smart contract,"
        " en expliquant brièvement les fonctionnalités et points clés."
    )
