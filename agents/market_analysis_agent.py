# agents/market_analysis_agent.py

from llm.gemini_wrapper import GeminiLLM
from config.settings import settings
import json
import os


class MarketAnalysisAgent:
    def __init__(self, prompt_path="llm/prompts/market_prompt.txt", data_path="data/market_news.json"):
        self.prompt_path = prompt_path
        self.data_path = data_path
        self.llm = GeminiLLM(api_key=settings.GEMINI_API_KEY)

    def load_market_data(self):
        """Loads external market data from JSON file"""
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Market data file not found: {self.data_path}")
        with open(self.data_path, 'r') as f:
            return json.load(f)

    def load_prompt_template(self):
        """Loads the agent's instruction prompt"""
        if not os.path.exists(self.prompt_path):
            raise FileNotFoundError(f"Prompt file not found: {self.prompt_path}")
        with open(self.prompt_path, 'r') as f:
            return f.read()

    def analyze_market(self):
        """Main method to analyze market data and return insights"""
        market_data = self.load_market_data()
        prompt_template = self.load_prompt_template()

        combined_input = f"{prompt_template}\n\nMarket News:\n{json.dumps(market_data, indent=2)}"
        print("Running market analysis using Gemini...")

        response = self.llm.generate_response(combined_input)
        return response


# Example usage (if run directly)
if __name__ == "__main__":
    agent = MarketAnalysisAgent()
    insights = agent.analyze_market()
    print("🔍 Market Risk Insights:\n", insights)
