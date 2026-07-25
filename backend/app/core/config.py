from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str
    ENVIRONMENT: str

    class Config:
        env_file = ".env"


settings = Settings()