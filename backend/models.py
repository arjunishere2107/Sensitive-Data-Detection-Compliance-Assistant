from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


class RiskResponse(BaseModel):
    risk: str
    score: int