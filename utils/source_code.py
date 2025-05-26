from .etherscan import get_contract_source as get_contract_source_code

def load_source_from_file(uploaded_file):
    """
    Charge le code source depuis un fichier .sol uploadé sur Streamlit.
    """
    return uploaded_file.read().decode("utf-8")
