from abc import ABC, abstractmethod
from langchain_core.documents import Document

class VectorStorePort(ABC):
    @abstractmethod
    def add_documents(self, documents: list[Document]):
        pass
