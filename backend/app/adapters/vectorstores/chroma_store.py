from langchain_chroma import Chroma
from app.domain.ports.vector_store_port import VectorStorePort

class ChromaStoreAdapter(VectorStorePort):
    def __init__(self, embedding):
        self.embedding = embedding
        self.db = Chroma(
            collection_name="hefesto_db",
            embedding_function=embedding.model,
            persist_directory="./chroma_db",
        )

    def add_documents(self, documents):
        self.db.add_documents(documents)
