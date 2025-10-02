from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from app.routes import router as code_router
from app.services import code_explainer
import time
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

# Create FastAPI app with enhanced configuration
app = FastAPI(
    title="LLM-Powered Code Reviewer",
    description="An AI-powered code explanation and review service",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Health check endpoint
@app.get("/healthz", tags=["Health"])
async def health_check():
    """Health check endpoint to verify service status"""
    logger.info("Health check endpoint accessed")
    response = {
        "status": "healthy",
        "timestamp": time.time(),
        "service": "LLM-Powered Code Reviewer",
        "version": "1.0.0"
    }
    logger.info(f"Health check response: {response}")
    return response

# Demo endpoint
@app.get("/demo", tags=["Demo"])
async def demo():
    """Demo endpoint that shows a sample code explanation"""
    logger.info("Demo endpoint accessed")
    sample_code = '''
def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def main():
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()
'''
    
    try:
        logger.info("Calling actual code_explainer service for demo")
        result = code_explainer(sample_code)
        logger.info("Code explanation generated successfully from actual service")
        
        response = {
            "message": "Demo code explanation generated successfully",
            "sample_code": sample_code,
            "explanation": result
        }
        logger.info("Demo endpoint response generated successfully")
        logger.debug(f"Demo response: {response}")
        return response
    except Exception as e:
        logger.error(f"Demo failed with actual service: {str(e)}")
        # Fallback to mock response if actual service fails
        logger.info("Falling back to mock response due to service error")
        mock_result = {
            "explanation": """This code implements the Fibonacci sequence calculation using recursion.

            **Function Breakdown:**
            1. `fibonacci(n)` - Recursive function that calculates the nth Fibonacci number
            - Base case: if n <= 1, return n (for n=0 returns 0, n=1 returns 1)
            - Recursive case: returns sum of previous two Fibonacci numbers
            
            2. `main()` - Driver function that prints first 10 Fibonacci numbers
            - Uses a for loop to iterate from 0 to 9
            - Calls fibonacci() for each number and prints the result
            
            3. `if __name__ == "__main__":` - Ensures main() only runs when script is executed directly""",
            
            "summary": "This is a classic recursive implementation of the Fibonacci sequence that calculates and prints the first 10 Fibonacci numbers. The algorithm uses the mathematical definition where each number is the sum of the two preceding ones, with base cases for 0 and 1."
        }
        
        response = {
            "message": "Demo code explanation generated successfully (fallback mock response)",
            "sample_code": sample_code,
            "explanation": mock_result
        }
        logger.info("Demo endpoint fallback response generated")
        return response

# API routes
logger.info("Including code router")
app.include_router(code_router)

# Serve frontend
logger.info("Mounting static files")
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"Starting server on port {port}")
    logger.info("Application startup complete")
    uvicorn.run(app, host="0.0.0.0", port=port)