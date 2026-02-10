from datetime import datetime

from pydantic import BaseModel


class ChatResponse(BaseModel):
    answer: str
    created: datetime = datetime.now()

    class Config:
        from_attributes = True


class AskToChat(BaseModel):
    question: str
    created: datetime = datetime.now()

    class Config:
        from_attributes = True
