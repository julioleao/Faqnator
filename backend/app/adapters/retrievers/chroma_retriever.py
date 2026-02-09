from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from app.domain.ports.retriever_port import RetrieverPort

class ChromaRetrieverAdapter(RetrieverPort):
    def __init__(self):
        embeddings = OllamaEmbeddings(
            model="nomic-embed-text"
        )

        self.vectorstore = Chroma(
            collection_name="hefesto_db",
            persist_directory="./chroma_db",
            embedding_function=embeddings
        )

        self.retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

    async def retrieve(self, query: str, k: int = 4):
        return await self.retriever.ainvoke(query)
