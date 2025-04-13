# llm/gemini_wrapper.py

import google.generativeai as genai
from config.settings import settings


class GeminiLLM:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.model = "gemini-2.0-flash"
        self._initialize_model()

    def _initialize_model(self):
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"[ERROR from Gemini API] {str(e)}"
