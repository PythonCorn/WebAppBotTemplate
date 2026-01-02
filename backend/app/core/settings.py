from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """MAIN SETTING"""
    ENV: str = "dev"
    """TELEGRAM BOT"""
    BOT_TOKEN: str
    BOT_WEBHOOK: str = "/bot"
    """HTTP"""
    PUBLIC_URL: Optional[str] = ""
    NGROK_AUTHTOKEN: Optional[str] = None
    """DATABASE"""
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    """PAYMENTS"""
    CRYPTOBOT_TURN_ON: bool = False
    CRYPTOBOT_WEBHOOK: str = "/cryptobot"
    CRYPTOBOT_TOKEN: Optional[str] = None
    IS_TEST_CRYPTOBOT: bool = True
    XROCKET_TURN_ON: bool = False
    XROCKET_WEBHOOK: str = "/xrocket"
    XROCKET_TOKEN: Optional[str] = None
    """REDIS"""
    REDIS_HOST: Optional[str] = "redis"
    REDIS_PORT: Optional[int] = 6379
    REDIS_DB: Optional[int] = 0

    @property
    def _get_db_url(self):
        return f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@db:5432/{self.POSTGRES_DB}"

    @property
    def async_db_url(self):
        return f"postgresql+asyncpg://{self._get_db_url}"

    @property
    def sync_db_url(self):
        return f"postgresql+psycopg2://{self._get_db_url}"

    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
