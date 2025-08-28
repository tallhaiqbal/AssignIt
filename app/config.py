from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str 
    database_username: str 
    database_password: str 
    database_name: str
    Secret_Key: str 
    Algorithm: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings() # type: ignore
