import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

from utils.source_code import get_contract_source_code, load_source_from_file
from utils.description import generate_description
from utils.badge_generator import extract_badges
from utils.market_data import get_token_data
from utils.summarizer import summarize_code
from utils.pdf_export import render_pdf

st.set_page_config(page_title="🔍 AI Smart Contract Analyzer", layout="wide")
st.title("🔍 AI Smart Contract Analyzer")

mode = st.radio(
    "Choose how to import the smart contract:",
    ("Ethereum Address", ".sol File")
)

code_source = ""
address = ""
market_data = {}

if mode == "Ethereum Address":
    address = st.text_input("Enter the smart contract Ethereum address:")
    if address:
        code_source = get_contract_source_code(address)
        if code_source:
            st.success("✅ Code successfully fetched from Etherscan.")
            market_data = get_token_data()
        else:
            st.error("❌ Failed to fetch code from Etherscan.")
elif mode == ".sol File":
    uploaded = st.file_uploader("Upload a .sol file", type="sol")
    if uploaded:
        code_source = load_source_from_file(uploaded)
        st.success("✅ .sol file successfully loaded.")


if code_source:
    with st.expander("📄 View Source Code"):
        st.code(code_source, language="solidity")


    description = generate_description(code_source)
    badges      = extract_badges(code_source)
    summary     = summarize_code(code_source)


    st.session_state["description"] = description
    st.session_state["badges"]      = badges
    st.session_state["summary"]     = summary
    st.session_state["market_data"] = market_data

    # Affichage
    st.markdown(st.session_state["description"])
    st.markdown("### 🏷 Detected Functional Badges")
    st.markdown(st.session_state["badges"])

    if market_data:
        st.markdown("### 📊 Real-Time Market Data (CoinGecko)")
        st.markdown(
            f"- **Name** : {market_data.get('name','-')}\n"
            f"- **Symbol** : {market_data.get('symbol','-')}\n"
            f"- **Current Price** : {market_data.get('current_price','-')} $\n"
            f"- **MarketCap** : {market_data.get('market_cap','-')} $"
        )

    st.markdown("### 🔎 Smart Contract Summary")
    st.info(st.session_state["summary"])

    st.markdown("### ❓ Ask a question about the contract")
    question = st.text_input("Your question:")
    if question:
        st.info(summarize_code(code_source, question))

    # Export PDF
    if st.button("📄 Export Analysis as PDF"):
        pdf_bytes = render_pdf(
            description=st.session_state["description"],
            badges=st.session_state["badges"],
            market_data=st.session_state["market_data"],
            summary=st.session_state["summary"],
            source_code=code_source,
        )
        st.download_button(
            label="💾 Download PDF",
            data=pdf_bytes,
            file_name="smart_contract_analysis.pdf",
            mime="application/pdf"
        )
