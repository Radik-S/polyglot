from os import path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    HOST: str = '0.0.0.0'
    PORT: int = 8080
    IS_DEV_MODE: bool = False

    SECRET_KEY_FOR_ENCRYPT_SESSION: str
    # Secure - только HTTPS
    SESSION_COOKIE_SECURE: bool = True,

    # HttpOnly - недоступен из JavaScript
    SESSION_COOKIE_HTTPONLY: bool = True,

    # SameSite - защита от CSRF
    SESSION_COOKIE_SAMESITE: str = 'Lax',  # или 'Strict'

    # Домен - ограничить домен
    SESSION_COOKIE_DOMAIN: str

    # Максимальный возраст # 1 час
    PERMANENT_SESSION_LIFETIME: int = 3600

    @property
    def get_path_templates(self):
        file_path = path.join('polyglot', 'adapters', 'http', 'templates')
        return path.abspath(file_path)

    @property
    def to_flask_config(self) -> dict:
        return {
            "SECRET_KEY": self.SECRET_KEY_FOR_ENCRYPT_SESSION,
            "SESSION_COOKIE_SECURE": self.SESSION_COOKIE_SECURE,
            "SESSION_COOKIE_HTTPONLY": self.SESSION_COOKIE_HTTPONLY,
            "SESSION_COOKIE_SAMESITE": self.SESSION_COOKIE_SAMESITE,
            "SESSION_COOKIE_DOMAIN": self.SESSION_COOKIE_DOMAIN,
            "PERMANENT_SESSION_LIFETIME": self.PERMANENT_SESSION_LIFETIME,
        }
