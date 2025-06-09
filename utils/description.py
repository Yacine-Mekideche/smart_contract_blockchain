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
        "You are a blockchain expert. Here's the full Solidity contract.\n"
        + header +
        "Analyze it and generate a professional summary like on CoinMarketCap, with:\n"
        "🧠 Brief Project Description\n"
        "🎯 Use Cases / Purpose\n"
        "🛠️ Technical Features\n"
        "🧾 Issuer or Organization (deployer address if available)\n"
        "🌍 Networks and Deployed Chains\n"
        "📅 Creation / Deployment Date\n"
        "📊 Neutral Summary, clear and without hallucinations\n"
        "🔖 Functional Badges (Markdown list)\n"
        "💼 Risks or Red Flags\n"
        "🧮 Tokenomics (if detectable)\n\n"
        f"Here is the code:\n```solidity\n{truncated}\n```\n"
        "Reply in English, concisely and professionally."
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
