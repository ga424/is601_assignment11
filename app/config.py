from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./module11.db"
    model_config = SettingsConfigDict(env_file=("local.env", ".env"))


settings = Settings()
