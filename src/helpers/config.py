from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name:str
    app_version:str
    key:str
    File_Allowed_Types:list
    File_Max_Size:int

    model_config = SettingsConfigDict(env_file=".env")

        
def get_settings():
    return Settings()