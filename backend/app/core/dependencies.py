from app.adapters.loaders.generic_loader import GenericLoaderAdapter
from app.adapters.loaders.markdown_loader import MarkdownLoaderAdapter
from app.adapters.embeddings.ollama_embeddings import OllamaEmbeddingAdapter
from app.adapters.vectorstores.chroma_store import ChromaStoreAdapter
from app.domain.services.ingest_service import IngestService
from app.adapters.llm.gemini_llm import GeminiLLMAdapter
from app.adapters.retrievers.chroma_retriever import ChromaRetrieverAdapter
from app.domain.services.chat_service import ChatService

def get_ingest_service():
    embedding_adapter = OllamaEmbeddingAdapter()

    vector_store = ChromaStoreAdapter(
        embedding=embedding_adapter
    )

    loader = GenericLoaderAdapter()

    return IngestService(
        loader=loader,
        vector_store=vector_store,
    )

def get_chat_service():
    llm = GeminiLLMAdapter()
    retriever = ChromaRetrieverAdapter()

    return ChatService(
        llm=llm,
        retriever=retriever
    )
