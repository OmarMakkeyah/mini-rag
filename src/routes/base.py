from fastapi import FastAPI, APIRouter ,Depends
from helpers.config import get_settings , Settings


base_router = APIRouter()

@base_router.get("/")
async def welcome(settings: Settings = Depends(get_settings)):
    APP_NAME = settings.app_name
    APP_VERSION = settings.app_version
    
    return {
        "APP_NAME": APP_NAME,
        "APP_VERSION": APP_VERSION
    }
