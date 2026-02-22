from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MINIO_ENDPOINT: str = "http://localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET: str = "polyglot"
    PRESIGNED_URL_EXPIRES_IN_SECONDS: int = 3600

    class Config:
        env_prefix = ""
