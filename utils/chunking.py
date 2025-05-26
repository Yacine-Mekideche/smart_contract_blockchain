from langchain.text_splitter import CharacterTextSplitter

def split_solidity_code(code: str):
    """
    Découpe le code Solidity en morceaux pour faciliter l’indexation vectorielle.
    """
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len
    )
    return splitter.split_text(code)
