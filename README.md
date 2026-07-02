# 🛡 Sensitive Data Detection & Compliance Assistant

## Overview

Sensitive Data Detection & Compliance Assistant is an AI-powered application that automatically detects confidential information inside uploaded documents, classifies the document's security risk, generates compliance reports, and allows users to interact with the document using Retrieval-Augmented Generation (RAG).

The application supports PDF, TXT, and CSV documents and leverages Large Language Models (LLMs), semantic search, and vector databases to provide intelligent document analysis.

---

## Features

- Upload PDF, TXT and CSV files
- Detect sensitive information
  - Aadhaar Number
  - PAN Number
  - Email Address
  - Phone Number
  - Credit Card Number
  - Bank Account Number
  - API Keys
  - Passwords
  - Employee IDs
- Risk Classification
  - Low
  - Medium
  - High
- AI-generated Compliance Summary
- RAG-based Question Answering
- PDF Compliance Report Generation
- Streamlit UI
- FastAPI Backend
- FAISS Vector Database

---

## Tech Stack

### Backend

- FastAPI
- Python
- LangChain
- FAISS
- Sentence Transformers
- Groq LLM
- ReportLab

### Frontend

- Streamlit

### AI Stack

- Llama 3.3 70B (Groq)
- all-MiniLM-L6-v2 Embeddings
- Retrieval-Augmented Generation (RAG)

---

## Project Structure

```
SensitiveDataAssistant
│
├── backend
├── frontend
├── docs
├── README.md
└── Dockerfile
```

---

## Installation

```bash
git clone <repository-url>

cd SensitiveDataAssistant

python -m venv venv

venv\Scripts\activate

pip install -r backend/requirements.txt

cd backend

uvicorn app:app --reload
```

Frontend

```bash
cd frontend

streamlit run app.py
```

---

## API Endpoints

| Endpoint | Description |
|-----------|-------------|
| POST /upload | Upload document |
| POST /chat | Ask questions |
| POST /report | Download report |

---

## AI Pipeline

Document Upload

↓

Document Parser

↓

Sensitive Data Detection (Regex)

↓

Risk Classification

↓

Text Chunking

↓

Embedding Generation

↓

FAISS Vector Database

↓

LLM Summary

↓

RAG Question Answering

↓

PDF Report Generation

---

## Future Improvements

- OCR Support
- Multi-document RAG
- Data Redaction
- Docker Deployment
- Kubernetes Deployment
- Audit Logging
- Authentication
- RBAC

---

## Author

Arjun Bhardwaj