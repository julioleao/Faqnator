from langchain_ollama import OllamaEmbeddings
from app.domain.ports.embedding_port import EmbeddingPort

class OllamaEmbeddingAdapter(EmbeddingPort):
    def __init__(self):
        self.model = OllamaEmbeddings(model="nomic-embed-text")

    def embed_documents(self, texts: list[str]):
        return self.model.embed_documents(texts)
