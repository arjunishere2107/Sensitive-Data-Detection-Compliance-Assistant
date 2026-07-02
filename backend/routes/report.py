import uuid

from fastapi import APIRouter
from pydantic import BaseModel

from detector import SensitiveDataDetector
from summarizer import ComplianceSummarizer
from services.report_service import ReportService

router = APIRouter()


class SummaryRequest(BaseModel):
    filename: str
    text: str


@router.post("/")
async def generate_summary(request: SummaryRequest):

    # Step 1: Detect sensitive data
    detection = SensitiveDataDetector.detect(request.text)

    # Step 2: Generate AI summary
    summary = ComplianceSummarizer.generate(
        request.text,
        detection
    )

    # Step 3: Generate unique report ID
    document_id = str(uuid.uuid4())

    # Step 4: Generate PDF report
    pdf_path = ReportService.generate_report(
        document_id=document_id,
        filename=request.filename,
        detection=detection,
        summary=summary
    )

    # Step 5: Return response
    return {

        "status": "success",

        "document_id": document_id,

        "detection": detection,

        "summary": summary,

        "report_path": pdf_path

    }