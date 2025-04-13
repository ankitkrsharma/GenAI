# agents/risk_scoring_agent.py

from llm.gemini_wrapper import GeminiLLM
from config.settings import settings
import json
import os


class RiskScoringAgent:
    def __init__(self, prompt_path="llm/prompts/scoring_prompt.txt", data_path="data/internal_data.json"):
        self.prompt_path = prompt_path
        self.data_path = data_path
        self.llm = GeminiLLM(api_key=settings.GEMINI_API_KEY)

    def load_internal_data(self):
        """Loads project metrics or transaction data"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Internal data file not found: {self.data_path}")
        with open(self.data_path, 'r') as f:
            return json.load(f)

    def load_prompt_template(self):
        """Loads the scoring prompt template"""
        if not os.path.exists(self.prompt_path):
            raise FileNotFoundError(f"Prompt file not found: {self.prompt_path}")
        with open(self.prompt_path, 'r') as f:
            return f.read()

    def score_risks(self):
        """Analyzes internal data and scores the project risk"""
        internal_data = self.load_internal_data()
        prompt_template = self.load_prompt_template()

        combined_input = f"{prompt_template}\n\nProject Metrics:\n{json.dumps(internal_data, indent=2)}"
        print("🧮 Scoring internal project risk using Gemini...")

        response = self.llm.generate_response(combined_input)
        return response


# Example usage
if __name__ == "__main__":
    agent = RiskScoringAgent()
    result = agent.score_risks()
    print("📉 Risk Scoring Report:\n", result)
