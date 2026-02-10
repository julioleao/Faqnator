from langchain_text_splitters import RecursiveCharacterTextSplitter

class IngestService:
    def __init__(
        self,
        loader,
        vector_store,
        chunk_size=1500,
        chunk_overlap=200,
    ):
        self.loader = loader
        self.vector_store = vector_store
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def ingest(self, path_or_filetext: str):
        docs = self.loader.load(path_or_filetext)

        chunks = self.splitter.split_documents(docs)

        self.vector_store.add_documents(chunks)
