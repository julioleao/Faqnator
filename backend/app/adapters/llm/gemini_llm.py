from langchain_google_genai import ChatGoogleGenerativeAI
from app.domain.ports.llm_port import LLMPort
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


class GeminiLLMAdapter(LLMPort):
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2,
        )

    async def generate(self, prompt: str) -> str:
        resp = await self.model.ainvoke(prompt)
        return resp.content
