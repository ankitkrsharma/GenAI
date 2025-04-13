from utils.gemini_client import GeminiClient  # assuming you have one
import os
import json

class ContextRetriever:
    def __init__(self, context_file="data/project_docs.json"):
        self.context_file = context_file
        if not os.path.exists(self.context_file):
            with open(self.context_file, 'w') as f:
                json.dump([], f)

    def add_documents(self, documents):
        """Save context data locally (as Gemini has no internal store)"""
        existing = self.load_documents()
        all_docs = existing + documents
        with open(self.context_file, 'w') as f:
            json.dump(all_docs, f, indent=2)

    def load_documents(self):
        with open(self.context_file, 'r') as f:
            return json.load(f)

    def get_relevant_context(self, query, top_k=3):
        """Basic keyword match or you can integrate semantic search"""
        all_docs = self.load_documents()
        relevant = sorted(
            all_docs,
            key=lambda doc: query.lower() in doc.lower(),
            reverse=True
        )
        return relevant[:top_k]

    def ask_gemini(self, query):
        context = self.get_relevant_context(query)
        prompt = f"""Based on the following internal context:

{chr(10).join(context)}

Answer the question: {query}
"""
        client = GeminiClient()
        return client.ask(prompt)
