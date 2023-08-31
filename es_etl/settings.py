from functools import lru_cache

from pydantic import BaseSettings, Field


class RedisSettings(BaseSettings):
    host: str | None = Field(None, env="redis_host")
    port: str | None = Field(None, env="redis_port")
    password: str | None = Field(None, env="redis_pass")


class PGSettings(BaseSettings):
    host: str | None = Field("db", env="DB_HOST")
    port: str | None = Field(None, env="pg_port")
    password: str | None = Field(None, env="pg_pass")
    user: str | None = Field(None, env="pg_user")
    dbname: str | None = Field(None, env="pg_db")


class ESSettings(BaseSettings):
    host: str | None = Field(None, env="elastic_host")
    port: str | None = Field(None, env="elastic_port")


class BackoffSettings(BaseSettings):
    start_sleep_time: float = Field(0.1, env="START_SLEEP_TIME")
    sleep_factor: int = Field(2, env="SLEEP_FACTOR")
    border_sleep_time: int = Field(2, env="BORDER_SLEEP_TIME")


class Settings(BaseSettings):
    redis: RedisSettings = RedisSettings()
    pg: PGSettings = PGSettings()
    es: ESSettings = ESSettings()
    backoff: BackoffSettings = BackoffSettings()
    batch_size: int = Field(100, env="BATCH_SIZE")
    use_redis_storage: bool = Field(True, env="USE_REDIS_STORAGE")
    automatic_updates: bool = Field(True, env="AUTOMATIC_UPDATES")


@lru_cache
def get_settings() -> Settings:
    return Settings()
