# Application Workflow

## Step 1

User uploads a document.

↓

## Step 2

Document Parser extracts text.

↓

## Step 3

Regex Engine detects:

- Aadhaar
- PAN
- Email
- Phone
- Credit Card
- Bank Details
- API Keys
- Passwords

↓

## Step 4

Risk Classifier assigns:

- Low
- Medium
- High

↓

## Step 5

Text is split into chunks.

↓

## Step 6

Embeddings are generated.

↓

## Step 7

Chunks are stored in FAISS.

↓

## Step 8

Groq LLM generates:

- Compliance Summary
- Security Risks
- Suggested Actions

↓

## Step 9

Users ask questions using RAG.

↓

## Step 10

PDF Compliance Report is generated.