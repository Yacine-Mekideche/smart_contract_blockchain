from .etherscan import get_contract_source as get_contract_source_code

def load_source_from_file(uploaded_file):
    return uploaded_file.read().decode("utf-8")
