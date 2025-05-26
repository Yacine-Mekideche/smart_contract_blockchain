import os
import requests

def get_contract_source(address: str) -> str:
    """
    Récupère le code source d'un smart contract sur Etherscan.
    """
    key = os.getenv("ETHERSCAN_API_KEY")
    if not key:
        raise ValueError("Clé API Etherscan manquante.")
    url = (
        "https://api.etherscan.io/api"
        f"?module=contract&action=getsourcecode&address={address}"
        f"&apikey={key}"
    )
    data = requests.get(url).json()
    if data.get("status") == "1" and data.get("result"):
        return data["result"][0]["SourceCode"]
    return None
