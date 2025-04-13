# File: config/settings.py

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load .env variables
load_dotenv()


class Settings(BaseSettings):
    # === Gemini ===
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

    # === Pinecone (optional) ===
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV: str = os.getenv("PINECONE_ENV")

    # === Langchain (optional) ===
    LANGCHAIN_API_KEY: str = os.getenv("LANGCHAIN_API_KEY")

    # === MySQL ===
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT: int = int(os.getenv("MYSQL_PORT", 3306))
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE", "project_risk_db")

    # === SQLAlchemy URL if needed ===
    @property
    def DB_URL(self):
        return (
            f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )


# Create a settings instance you can import everywhere
settings = Settings()
