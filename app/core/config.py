import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "Deployment Service"
    api_v1_prefix: str = "/api/v1"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./deployments.db")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"


settings = Settings()
