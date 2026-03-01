import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.extractor import extract_invoice_data
from models.schemas import ExtractionRequest, ExtractionResult

# Setup Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="LLM Unstructured Data Extractor",
    description="Enterprise API for transforming chaotic text (PDF OCR/Emails) into strictly typed JSON using AI.",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "Operational", "service": "LLM Extractor"}

@app.post("/api/v1/extract/invoice", response_model=ExtractionResult, tags=["Data Extraction"])
async def process_extraction(request: ExtractionRequest):
    """
    Endpoint to push raw unstructured text and retrieve validated JSON structure.
    """
    try:
        logger.info(f"Received extraction request. Text length: {len(request.raw_text)}")
        result = await extract_invoice_data(request.raw_text)
        return result
    except Exception as e:
        logger.error(f"Extraction failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process text via LLM. Please check logs.")

if __name__ == "__main__":
    import uvicorn
    # Make sure to run with: uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8080)