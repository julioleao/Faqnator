from langchain_community.document_loaders import UnstructuredMarkdownLoader
from app.domain.ports.document_loader_port import DocumentLoaderPort

class MarkdownLoaderAdapter(DocumentLoaderPort):
    def load(self, path: str):
        loader = UnstructuredMarkdownLoader(
            path,
            mode="single",
            strategy="fast",
        )
        return loader.load()
