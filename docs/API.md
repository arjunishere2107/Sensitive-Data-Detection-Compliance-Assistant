# API Documentation

## Upload Document

POST /upload

### Request

multipart/form-data

file=<document>

### Response

```json
{
  "document_id": "...",
  "filename": "...",
  "detections": {},
  "preview": "...",
  "report": "..."
}
```

---

## Chat

POST /chat

### Request

```json
{
  "document_id":"...",
  "question":"Summarize the document"
}
```

### Response

```json
{
    "answer":"..."
}
```

---

## Report

POST /report

Returns PDF compliance report.