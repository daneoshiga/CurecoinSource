from pathlib import Path

from pydantic import BaseSettings

path = Path(__file__).parent.absolute()


class Settings(BaseSettings):
    QUOTE_ROOT_URL: str

    class Config:
        env_file = path / ".." / ".env"


settings = Settings()
