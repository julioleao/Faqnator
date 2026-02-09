class ChatService:
    def __init__(
        self,
        llm,
        retriever,
    ):
        self.llm = llm
        self.retriever = retriever

    async def ask(self, question: str) -> str:
        docs = await self.retriever.retrieve(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
Você é um assistente técnico especializado em análise de documentação.

Regras obrigatórias:
- Utilize EXCLUSIVAMENTE as informações do CONTEXTO
- NÃO faça suposições
- Seja direto e técnico

CONTEXTO:
{context}

PERGUNTA:
{question}
"""

        return await self.llm.generate(prompt)
