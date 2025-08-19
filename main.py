from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router as code_router

app = FastAPI(title="LLM Code Explainer")

# API routes
app.include_router(code_router)

# Serve frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")
