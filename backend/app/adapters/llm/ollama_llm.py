from app.domain.ports.llm_port import LLMPort

class OllamaLLM(LLMPort):
    def __init__(self, client):
        self.client = client

    async def generate(self, prompt: str) -> str:
        resp = await self.client.generate(
            model="llama3",
            prompt=prompt
        )
        return resp["response"]
