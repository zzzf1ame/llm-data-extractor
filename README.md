# 🧩 Enterprise LLM Data Extractor API
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103%2B-00a393.svg)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-orange.svg)](https://python.langchain.com)
[![Pydantic](https://img.shields.io/badge/Pydantic-V2-E92063.svg)](https://docs.pydantic.dev)
A production-ready asynchronous microservice that leverages Large Language Models (LLMs) and Pydantic to transform highly unstructured text (like OCR dumps, scattered emails, and chaotic receipts) into **strictly typed, predictable JSON data**.
## 🚀 The Business Problem Checked
In modern workflows, companies receive unstructured data daily (invoices, resumes, contracts). Hardcoded Regex fails when formats change. This API uses AI Function Calling (`with_structured_output`) to intelligently parse fields regardless of the text layout, with zero hallucination.
## 🏗 System Architecture
* **Framework:** `FastAPI` (Fully Async)
* **AI Orchestration:** `LangChain`
* **Validation:** `Pydantic V2` Schema enforcement
* **LLM Engine:** OpenAI `gpt-4o-mini` (Configurable)
## ⚡ Quick Start
### 1. Installation
```bash
git clone https://github.com/your-username/llm-data-extractor.git
cd llm-data-extractor
pip install -r requirements.txt