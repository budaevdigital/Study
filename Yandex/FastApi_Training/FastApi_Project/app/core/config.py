# app/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "..."
    app_description: str = "..."

    class Config:
        env_file = ".env"


settings = Settings()
