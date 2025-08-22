# 🧑‍💻 LLM Code Explainer

LLM-powered tool that explains code with **step-by-step explanations**, **flow diagrams** (Mermaid), and **concise summaries**.  
Supports both **pasting code** and **uploading files** through a simple web UI.  

---

## 🚀 Features
- 🔍 Explain any code (Python, JS, Java, C++, etc.)
- 📊 Auto-generate **flow diagrams** in Mermaid
- ✍️ Produce **2–3 sentence summaries**
- 🌐 Web frontend with **paste + file upload**
- 📋 Copy-to-clipboard for all outputs
- ⚡ FastAPI backend powered by **Ollama LLM**

---

## 🏗️ Project Structure
llm-code-explainer/
│── main.py # FastAPI entrypoint
│── requirements.txt # Dependencies
│── README.md # This file
│
├── app/
│ ├── routes.py # API endpoints (/explain)
│ ├── services.py # LLM logic (Ollama prompt + cleaning)
│ └── schemas.py # (placeholder for future models)
│
└── static/
└ ── index.html # Frontend (paste + file upload UI)

---

## ⚙️ Setup & Run
1️-> Setup environment
    ```bash
    conda create -n codeexplainer python=3.12 -y
    conda activate codeexplainer
    pip install -r requirements.txt
    ```

2️-> Run backend
    uvicorn main:app --reload

3️-> Open frontend
    Go to 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)  
    Paste code or upload a file  
    Get instant explanation + flow diagram + summary
