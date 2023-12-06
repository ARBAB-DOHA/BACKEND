from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str 
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    reset_token_expire_hours:int
    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    sender_email: str
    reset_password_url: str


    class Config:
        env_file = ".env"


settings = Settings()