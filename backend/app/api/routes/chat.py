from fastapi import APIRouter, Depends

from app.api.schemas import ChatResponse, AskToChat
from app.core.dependencies import get_chat_service

router = APIRouter()

@router.post("/chat")
async def chat(question: AskToChat, service=Depends(get_chat_service)):
    answer = await service.ask(question.question)

    return ChatResponse(
        answer=answer
    ).model_dump()
