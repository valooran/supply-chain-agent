import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str


def get_settings() -> Settings:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ConfigError(
            "ANTHROPIC_API_KEY is missing. Copy .env.example to .env and add your key."
        )
    model = os.getenv("MODEL_NAME", "claude-haiku-5-5")
    return Settings(api_key=api_key, model=model)