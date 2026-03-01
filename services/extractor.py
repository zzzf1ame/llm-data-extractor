import os
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models.schemas import ExtractionResult

load_dotenv()
logger = logging.getLogger(__name__)

# Initialize LLM. Using GPT-3.5-turbo or GPT-4o-mini for fast, cheap, reliable JSON extraction.
LLM_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

def get_extraction_llm():
    if not LLM_API_KEY:
        logger.warning("OPENAI_API_KEY is missing! LLM calls will fail.")
    return ChatOpenAI(
        model=MODEL_NAME, 
        temperature=0, 
        api_key=LLM_API_KEY
    ).with_structured_output(ExtractionResult)


# The System Prompt is engineered to force extraction without hallucination
system_prompt = """You are an expert data extraction algorithm.
Your job is to extract strict structured entity data from unstructured text, such as emails, receipts, or OCR text.
If any attribute is completely missing from the text and cannot be inferred, you should omit it or return a default/null value.
DO NOT make up data.
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Extract information from the following text:\n\n{text}")
])

async def extract_invoice_data(raw_text: str) -> ExtractionResult:
    """
    Asynchronously extracts structured data from raw text using Langchain and Pydantic.
    """
    logger.info("Initializing LLM layout extraction...")
    extractor = prompt_template | get_extraction_llm()
    
    # Run absolute async execution
    extracted_data = await extractor.ainvoke({"text": raw_text})
    return extracted_data