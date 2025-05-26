import os
from dotenv import load_dotenv
import streamlit as st

# Charge .env
load_dotenv()

# Import des utils
from utils.source_code import get_contract_source_code, load_source_from_file
from utils.description import generate_description
from utils.badge_generator import extract_badges
from utils.market_data import get_token_data
from utils.summarizer import summarize_code
from utils.pdf_export import render_pdf

st.set_page_config(page_title="🔍 Analyseur IA de Smart Contract", layout="wide")
st.title("🔍 Analyseur IA de Smart Contract")

mode = st.radio(
    "Choisissez la méthode d'importation du contrat :",
    ("Adresse Ethereum", "Fichier .sol")
)

code_source = ""
address = ""
market_data = {}

# --- Récupération du code source ---
if mode == "Adresse Ethereum":
    address = st.text_input("Entrez l'adresse du smart contract Ethereum :")
    if address:
        code_source = get_contract_source_code(address)
        if code_source:
            st.success("✅ Code récupéré avec succès depuis Etherscan.")
            market_data = get_token_data()
        else:
            st.error("❌ Impossible de récupérer le code depuis Etherscan.")
elif mode == "Fichier .sol":
    uploaded = st.file_uploader("Importez un fichier .sol", type="sol")
    if uploaded:
        code_source = load_source_from_file(uploaded)
        st.success("✅ Fichier .sol chargé avec succès.")

# --- Affichage et analyses ---
if code_source:
    with st.expander("📄 Voir le code source"):
        st.code(code_source, language="solidity")

    # Générations
    description = generate_description(code_source)
    badges      = extract_badges(code_source)
    summary     = summarize_code(code_source)

    # Sauvegarde en session (écrase toujours)
    st.session_state["description"] = description
    st.session_state["badges"]      = badges
    st.session_state["summary"]     = summary
    st.session_state["market_data"] = market_data

    # Affichage
    st.markdown(st.session_state["description"])
    st.markdown("### 🏷 Badges fonctionnels détectés")
    st.markdown(st.session_state["badges"])

    if market_data:
        st.markdown("### 📊 Données temps réel (CoinGecko)")
        st.markdown(
            f"- **Nom** : {market_data.get('name','-')}\n"
            f"- **Symbole** : {market_data.get('symbol','-')}\n"
            f"- **Prix actuel** : {market_data.get('current_price','-')} $\n"
            f"- **MarketCap** : {market_data.get('market_cap','-')} $"
        )

    st.markdown("### Résumé global du contrat")
    st.info(st.session_state["summary"])

    st.markdown("### ❓ Posez vos questions sur le contrat")
    question = st.text_input("Votre question :")
    if question:
        st.info(summarize_code(code_source, question))

    # Export PDF
    if st.button("📄 Exporter l'analyse en PDF"):
        pdf_bytes = render_pdf(
            description=st.session_state["description"],
            badges=st.session_state["badges"],
            market_data=st.session_state["market_data"],
            summary=st.session_state["summary"],
            source_code=code_source,
        )
        st.download_button(
            label="💾 Télécharger le PDF",
            data=pdf_bytes,
            file_name="smart_contract_analysis.pdf",
            mime="application/pdf"
        )
