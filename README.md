# 🔍 IAcine Smart Contract Analyzer | AI-Powered Ethereum Code Audit with RAG

![image](https://github.com/user-attachments/assets/2a0c3fbb-7306-4b15-b219-189b7d0ae476)


## 📖 Introduction

**IAcine Smart Contract Analyzer** is a powerful AI tool that analyzes Ethereum smart contracts directly from their source code. Using **RAG (Retrieval-Augmented Generation)**, OpenAI's GPT, and a modern Streamlit interface, it generates clean summaries, functional insights, and answers to any question you ask — all based on the real Solidity code.

Whether you're a blockchain developer, an auditor, or a business working with tokens and DeFi, this app turns code complexity into clarity. 🤖📜

---

## 🚀 Features

✔️ **Etherscan Integration** – Fetch smart contract code from any Ethereum address  
✔️ **CoinMarketCap-style Summaries** – Auto-generate project descriptions  
✔️ **Feature Detection** – Detects blacklist, pause, mint, burn, ownership, and upgradeability  
✔️ **Ask Anything with RAG** – Get AI answers based on the actual Solidity code  
✔️ **PDF Report Export** – Download a clean, structured audit-style report  
✔️ **Streamlit Web App** – User-friendly, no-code frontend to interact with AI

---

## 🏗️ Technologies

- 🐍 **Python 3.12** – App logic and backend  
- 🧠 **OpenAI GPT** – Large Language Model for summaries and QA  
- 🔍 **LangChain + FAISS** – Retrieval-Augmented Generation pipeline  
- 🌐 **Streamlit** – Lightweight frontend framework  
- 📂 **Etherscan & CoinGecko API** – For source code and market data  
- 📄 **FPDF** – Exporting structured audit-style PDFs  
- 🛡️ **dotenv** – Secure API key management

---

## 📦 Installation

### === 1️⃣ Clone the Repository
```bash
git clone https://github.com/Yacine-Mekideche/smart_contract_blockchain.git
cd smart_contract_blockchain
```

### === 2️⃣ Create a `.env` File
```env
OPENAI_API_KEY=your_openai_api_key
ETHERSCAN_API_KEY=your_etherscan_api_key
```

### === 3️⃣ Set Up Your Environment
```bash
python -m venv venv
# Activate:
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### === 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

Start the app with:
```bash
streamlit run app.py
```

Then open the Streamlit UI in your browser. You can:

- 🔍 Paste a smart contract address (e.g., `0xdAC17F958D2ee523a2206206994597C13D831ec7`)  
- 📄 Or upload a `.sol` file directly  
- ✅ Get badges, summaries, and ask your own questions  
- 📅 Export a PDF report

---

## 🎯 Demo

<a href="https://www.youtube.com/watch?v=koImlRDRiyU" target="_blank">
  <img src="https://img.youtube.com/vi/koImlRDRiyU/maxresdefault.jpg" alt="IAcine Smart Contract Analyzer Demo" style="max-width:100%; height:auto;">
</a>


---

## 🧠 AI Architecture Overview

- **Input** → Ethereum address or uploaded Solidity file  
- **Source Code** → Retrieved via Etherscan or Streamlit uploader  
- **RAG Pipeline** → FAISS + LangChain + OpenAI  
- **Outputs**:
  - Project Summary
  - Functional Badges
  - AI-Powered Q&A
  - PDF Report

---

## 📬 Contact Me

💡 **Into AI + Blockchain? Let’s build the future together.**

[![Website](https://img.shields.io/badge/My%20Website-%23000000.svg?style=for-the-badge&logo=About.me&logoColor=white)](https://iacine.tech)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yacine-mekideche/)  
[![GitHub](https://img.shields.io/badge/GitHub-%2312100E.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yacine-Mekideche)  
[![Malt](https://img.shields.io/badge/Malt-%23FF6F61.svg?style=for-the-badge&logo=malt&logoColor=white)](https://malt.fr/profile/yacinemekideche)  
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@iacine_tech)

📩 **Business inquiries:** contact@iacine.tech

---

**#SmartContracts #AI #Ethereum #RAG #LangChain #GPT #Solidity #Audit #Streamlit #OpenAI #DeFi #BlockchainSecurity #YacineTech #FreelanceAI #PythonProject**
