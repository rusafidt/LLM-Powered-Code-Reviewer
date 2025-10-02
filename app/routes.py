from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import code_explainer
from typing import Optional
import logging
from pydantic import BaseModel

# Configure logger for routes
logger = logging.getLogger(__name__)

# Pydantic model for text input
class CodeText(BaseModel):
    code: str

router = APIRouter(prefix="/explain", tags=["Code Explainer"])

@router.post("/")
async def explain_code(file: UploadFile = File(...)):
    """
    Explain code from uploaded file
    
    - **file**: Code file to analyze (.py, .js, .java, .cpp, .ts, .go, .rb, .cs)
    
    Returns explanation, diagram, and summary of the code
    """
    logger.info(f"File upload endpoint accessed with file: {file.filename}")
    try:
        code = (await file.read()).decode("utf-8")
        logger.info(f"File read successfully, size: {len(code)} characters")
        logger.debug(f"Code content preview: {code[:100]}...")
        
        result = code_explainer(code)
        logger.info("Code explanation generated successfully")
        
        response = {
            "success": True,
            "filename": file.filename,
            "file_size": len(code),
            "result": result
        }
        logger.info(f"Response prepared for file: {file.filename}")
        return response
    except Exception as e:
        logger.error(f"Code explanation failed for file {file.filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Code explanation failed: {str(e)}")

@router.post("/text")
async def explain_code_text(code_input: CodeText):
    """
    Explain code from text input
    
    - **code**: Code text to analyze
    
    Returns explanation, diagram, and summary of the code
    """
    logger.info("Text explanation endpoint accessed")
    try:
        code = code_input.code
        if not code.strip():
            logger.warning("Empty code text provided")
            raise HTTPException(status_code=400, detail="Code text cannot be empty")
        
        logger.info(f"Code text received, length: {len(code)} characters")
        logger.debug(f"Code content preview: {code[:100]}...")
        
        result = code_explainer(code)
        logger.info("Code explanation generated successfully")
        
        response = {
            "success": True,
            "code_length": len(code),
            "result": result
        }
        logger.info("Text explanation response prepared successfully")
        return response
    except Exception as e:
        logger.error(f"Code explanation failed for text input: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Code explanation failed: {str(e)}")

@router.get("/")
async def get_explain_info():
    """
    Get information about the code explanation service
    """
    logger.info("Service info endpoint accessed")
    response = {
        "service": "Code Explainer",
        "description": "AI-powered code explanation service",
        "supported_formats": [".py", ".js", ".java", ".cpp", ".ts", ".go", ".rb", ".cs"],
        "endpoints": {
            "POST /explain/": "Upload file for explanation",
            "POST /explain/text": "Submit code text for explanation",
            "GET /explain/": "Get service information"
        }
    }
    logger.info("Service info response prepared")
    return response
