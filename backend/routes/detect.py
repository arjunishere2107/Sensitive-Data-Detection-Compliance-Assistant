from fastapi import APIRouter
from pydantic import BaseModel

from detector import SensitiveDataDetector

router = APIRouter()


class DetectRequest(BaseModel):
    text: str


@router.post("/")
async def detect_sensitive_data(request: DetectRequest):

    results = SensitiveDataDetector.detect(request.text)

    return results