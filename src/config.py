"""Runtime settings, read from environment variables or a local .env file.

Every value has a safe default, so the app starts without any configuration.
Change behaviour per environment (laptop, Docker, CI) by setting variables, not by editing code.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Generation (path 2)
    llm_backend: Literal["ollama", "api", "mock"] = "ollama"
    llm_base_url: str = "http://localhost:11434/v1"
    llm_model: str = "qwen2.5:3b"

    # Retrieval (shared by path 1 and path 2: part of the contract)
    embedding_model: str = "intfloat/multilingual-e5-small"
    chroma_dir: str = "data/index/chroma"
    top_k: int = 3


@lru_cache
def get_settings() -> Settings:
    """Load settings once and reuse them."""
    return Settings()
