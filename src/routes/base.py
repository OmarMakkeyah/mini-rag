from fastapi import FastAPI, APIRouter
from helpers.config import get_settings

base_router = APIRouter()

@base_router.get("/")
async def welcome():
    APP_NAME = get_settings().app_name
    APP_VERSION = get_settings().app_version
    
    return {
        "APP_NAME": APP_NAME,
        "APP_VERSION": APP_VERSION
    }
