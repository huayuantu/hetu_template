from pydantic import PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings


class AllocationSettings(BaseSettings):
    DATABASE_URL: PostgresDsn = "postgresql://postgres:password@localhost:5432/postgres"  # type: ignore
    REDIS_URL: RedisDsn = "redis://redis:6379"  # type: ignore
    SMTP_HOST: str = "localhost"
    SMTP_PORT: int = 1025
