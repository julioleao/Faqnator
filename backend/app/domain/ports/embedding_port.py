from abc import ABC, abstractmethod

class EmbeddingPort(ABC):
    @abstractmethod
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        pass
