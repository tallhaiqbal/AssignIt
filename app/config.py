from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str 
    database_password: str 
    database_name: str
    database_username: str 
    Secret_Key: str 
    Algorithm: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings() # type: ignore