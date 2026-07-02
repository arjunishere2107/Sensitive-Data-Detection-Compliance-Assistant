from fastapi import APIRouter

from pydantic import BaseModel

from rag import RAGPipeline


router = APIRouter()


class ChatRequest(BaseModel):

    document_id: str

    question: str


@router.post("/")
async def chat(request:ChatRequest):

    answer=RAGPipeline.ask(
        
        request.document_id,

        request.question

    )

    return{
        
        "document_id": request.document_id,

        "question":request.question,

        "answer":answer

    }