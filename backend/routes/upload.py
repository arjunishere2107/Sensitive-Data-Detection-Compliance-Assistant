import os
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from parser import DocumentParser
from detector import SensitiveDataDetector
from summarizer import ComplianceSummarizer
from services.vector_service import VectorService
from services.report_service import ReportService

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document, parse it, detect sensitive information,
    generate AI summary, create a PDF report,
    build a FAISS vector database, and return the analysis.
    """

    try:
        # Generate unique document ID
        document_id = str(uuid.uuid4())

        # Preserve original extension
        extension = os.path.splitext(file.filename)[1]

        # Store uploaded file with unique name
        stored_filename = f"{document_id}{extension}"
        file_path = os.path.join(UPLOAD_FOLDER, stored_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Parse document
        extracted_text = DocumentParser.parse(file_path)

        # Detect sensitive information
        detection_results = SensitiveDataDetector.detect(extracted_text)

        # Generate AI Compliance Summary
        summary = ComplianceSummarizer.generate(
            extracted_text,
            detection_results
        )

        # Generate PDF Report
        report_path = ReportService.generate_report(
            document_id=document_id,
            filename=file.filename,
            detection=detection_results,
            summary=summary
        )

        # Create FAISS Vector Store
        chunk_count = VectorService.create_vector_store(
            document_id=document_id,
            text=extracted_text
        )

        # Return response
        return {
            "status": "success",
            "document_id": document_id,
            "filename": file.filename,
            "stored_filename": stored_filename,
            "file_type": extension,
            "characters": len(extracted_text),
            "chunks": chunk_count,
            "preview": extracted_text[:500],
            "detections": detection_results,
            "summary": summary,
            "report": report_path,
            "message": "Document uploaded, analyzed, indexed, and report generated successfully."
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error processing document: {str(e)}"
        )