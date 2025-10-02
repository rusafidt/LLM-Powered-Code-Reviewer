# 🧑‍💻 LLM Code Explainer

LLM-powered tool that explains code with **step-by-step explanations** and **concise summaries**.  
Supports both **pasting code** and **uploading files** through a sleek web UI.  

---

## 🚀 Features
- 🔍 Explain any code (Python, JS, Java, C++, etc.)
- ✍️ Produce **detailed explanations** and **2–3 sentence summaries**
- 🌐 Modern web frontend with **paste + file upload**
- 📋 Copy-to-clipboard for all outputs
- ⚡ FastAPI backend powered by **Hugging Face LLM**
- 🎨 Sleek, minimalistic design with responsive layout

---

## 🏗️ Project Structure
```
llm-code-explainer/
├── main.py              # FastAPI entrypoint
├── requirements.txt     # Dependencies
├── render.yaml         # Render deployment config
├── Procfile            # Alternative deployment
├── README.md           # This file
│
├── app/
│   ├── routes.py       # API endpoints (/explain)
│   ├── services.py     # LLM logic (Hugging Face API)
│   └── __init__.py
│
└── static/
    └── index.html      # Frontend (modern UI)
```

---

## ⚙️ Local Setup & Run

### 1️⃣ Setup environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Set up Hugging Face API Token
```bash
# Set your Hugging Face token
export HF_TOKEN="your_huggingface_token_here"
```

### 3️⃣ Run the application
```bash
# Method 1: Direct Python
python main.py

# Method 2: Uvicorn
uvicorn main:app --reload --port 8000
```

### 4️⃣ Open frontend  
👉 Go to [http://localhost:8000](http://localhost:8000)  
👉 Paste code or upload a file  
👉 Get instant explanation + summary

---

## 🔧 API Endpoints

- `GET /` - Main web interface
- `GET /healthz` - Health check
- `GET /demo` - Demo with sample code
- `GET /docs` - Interactive API documentation
- `POST /explain/` - Upload file for explanation
- `POST /explain/text` - Submit code text for explanation

---

## 🛠️ Development

### Adding new features
- **Backend**: Modify `app/routes.py` for new endpoints
- **Frontend**: Update `static/index.html` for UI changes
- **LLM Logic**: Customize prompts in `app/services.py`

### Testing
```bash
# Test health endpoint
curl http://localhost:8000/healthz

# Test demo endpoint
curl http://localhost:8000/demo
```

---

## 🚀 Live Demo

**Frontend:** [To-Do-List Link](https://llm-powered-code-reviewer.onrender.com/)

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Made with ❤️ using FastAPI + Hugging Face + Modern Web Technologies**