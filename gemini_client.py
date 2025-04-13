import os
import google.generativeai as genai


class GeminiClient:
    def __init__(self, model_name="models/embedding-001"):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            self.model = genai.get_model(model_name)
        except Exception as e:
            print(f"Error initializing Gemini model: {e}")
            self.model = None

    def embed_text(self, text: str):
        if not self.model:
            raise Exception("Gemini model is not initialized. Please check the API key and model name.")

        try:
            result = self.model.embed_content(
                content=text,
                task_type="retrieval_document"  # Or "retrieval_query" for queries
            )
            return result.get("embedding", None)
        except Exception as e:
            print(f"Error embedding text: {e}")
            return None
