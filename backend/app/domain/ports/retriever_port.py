from abc import ABC, abstractmethod
from langchain_core.documents import Document

class RetrieverPort(ABC):
    @abstractmethod
    async def retrieve(self, query: str, k: int = 4) -> list[Document]:
        pass
