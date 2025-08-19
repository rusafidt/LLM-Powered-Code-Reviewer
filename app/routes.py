from fastapi import APIRouter, UploadFile, File
from app.services import code_explainer

router = APIRouter(prefix="/explain", tags=["Code Explainer"])

@router.post("/")
async def explain_code(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8")
    result = code_explainer(code)
    return result
