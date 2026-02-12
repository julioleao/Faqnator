from langchain_ollama import ChatOllama

from app.domain.ports.llm_port import LLMPort


class OllamaLLMAdapter(LLMPort):
    def __init__(self):
        self.model = ChatOllama(
            model="gpt-oss:20b-cloud",
            temperature=0.2,
        )

    async def generate(self, prompt: str) -> str:
        resp = await self.model.ainvoke(prompt)
        return resp.content
