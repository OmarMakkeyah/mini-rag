from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name:str
    app_version:str
    key:str
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()