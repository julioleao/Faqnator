from abc import ABC, abstractmethod
from langchain_core.documents import Document

class DocumentLoaderPort(ABC):
    @abstractmethod
    def load(self, path_or_filetext: str) -> list[Document]:
        pass
