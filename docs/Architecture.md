# System Architecture

## Overview

The application follows a modular AI pipeline architecture.

```
User
   │
   ▼
Streamlit Frontend
   │
   ▼
FastAPI Backend
   │
   ├── Document Parser
   ├── Sensitive Data Detector
   ├── Risk Classifier
   ├── Embedding Generator
   ├── FAISS Vector Store
   ├── Groq LLM
   └── Report Generator
```

---

## Components

### Frontend

- Streamlit UI
- Upload documents
- Display detections
- Chat interface
- Report download

### Backend

- FastAPI REST APIs

### Parser

Supports:

- PDF
- TXT
- CSV

### Detection Engine

Regex-based sensitive data detection.

### Classification Engine

Assigns risk score based on detected entities.

### Vector Store

FAISS stores semantic embeddings for RAG.

### LLM

Groq Llama 3.3 70B generates:

- Compliance Summary
- Security Risks
- Suggested Remediation
- Chat Responses

### Report Generator

Creates downloadable PDF compliance reports.