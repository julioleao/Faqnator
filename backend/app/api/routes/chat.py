from fastapi import APIRouter, Depends
from app.core.dependencies import get_chat_service

router = APIRouter()

@router.post("/chat")
async def chat(question: str, service=Depends(get_chat_service)):
    answer = await service.ask(question)
    return {"answer": answer}
