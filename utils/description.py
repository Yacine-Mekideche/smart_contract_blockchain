import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(source_code: str, token_name: str = None, token_symbol: str = None) -> str:
    """
    Génère une fiche descriptive style CoinMarketCap à partir du code source Solidity.
    Si token_name/symbol fournis, les injecte en haut de la fiche.
    """
    truncated = source_code[:8000]
    header = ""
    if token_name:
        header += f"🔹 Nom du Token : {token_name}\n"
    if token_symbol:
        header += f"🔹 Symbole du Token : {token_symbol}\n"
    prompt = (
        "Tu es un expert blockchain. Voici un contrat Solidity complet.\n"
        + header +
        "Analyse-le et génère une fiche descriptive professionnelle, comme sur CoinMarketCap, avec :\n"
        "🧠 Description Brève du Projet\n"
        "🎯 Cas d’Usage / Objectif\n"
        "🛠️ Caractéristiques Techniques\n"
        "🧾 Émetteur ou Organisation (adresse déployeur si disponible)\n"
        "🌍 Réseaux et Chaînes Déployées\n"
        "📅 Date de Création / Déploiement\n"
        "📊 Résumé Neutre, clair, sans invention\n"
        "🔖 Badges fonctionnels (liste markdown)\n"
        "💼 Risques ou Points de Vigilance\n"
        "🧮 Tokenomics (si détectables)\n\n"
        f"Voici le code :\n```solidity\n{truncated}\n```\n"
        "Réponds en français, de façon concise."
    )

    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=1000
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Erreur lors de la génération : {e}"
