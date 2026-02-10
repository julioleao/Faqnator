from langchain_core.documents import Document
from app.domain.ports.document_loader_port import DocumentLoaderPort


class GenericLoaderAdapter(DocumentLoaderPort):
    def load(self, log_text: str =None):
        docs = [Document(page_content=log_text)]
        return docs
