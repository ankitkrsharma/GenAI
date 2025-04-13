# agents/project_tracking_agent.py

from llm.gemini_wrapper import GeminiLLM
from config.settings import settings
import json
import os


class ProjectTrackingAgent:
    def __init__(self, prompt_path="llm/prompts/status_prompt.txt", data_path="data/internal_data.json"):
        self.prompt_path = prompt_path
        self.data_path = data_path
        self.llm = GeminiLLM(api_key=settings.GEMINI_API_KEY)

    def load_internal_data(self):
        """Loads internal project metrics (status, delays, resources)"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Internal data file not found: {self.data_path}")
        with open(self.data_path, 'r') as f:
            return json.load(f)

    def load_prompt_template(self):
        """Loads project tracking instruction template"""
        if not os.path.exists(self.prompt_path):
            raise FileNotFoundError(f"Prompt file not found: {self.prompt_path}")
        with open(self.prompt_path, 'r') as f:
            return f.read()

    def track_project_status(self):
        """Uses LLM to analyze internal progress data and spot risks"""
        internal_data = self.load_internal_data()
        prompt_template = self.load_prompt_template()

        input_text = f"{prompt_template}\n\nInternal Metrics:\n{json.dumps(internal_data, indent=2)}"
        print("📊 Tracking project status using Gemini...")

        response = self.llm.generate_response(input_text)
        return response


# Example usage
if __name__ == "__main__":
    agent = ProjectTrackingAgent()
    insights = agent.track_project_status()
    print("🛠️ Project Tracking Insights:\n", insights)
