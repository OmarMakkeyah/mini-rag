from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import aiofiles
import os
import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(prefix= "/api/v1/data",tags=["api_v1","data"])

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str,file: UploadFile,app_settings: Settings = Depends(get_settings)):
    dataController = DataController()
    file_is_valid, signal_result= dataController.validate_uploaded_file(file= file)
    if not file_is_valid:
        return JSONResponse(
            content ={
                "signal":signal_result
            }
        )
        
    filePath, file_id = dataController.generate_unique_file_Path(orig_filename=file.filename,project_id=project_id)
    try:
        async with aiofiles.open(filePath,"wb") as f:
            while chunk:= await file.read(size=get_settings().FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(
        content= 
        {
            "signal": ResponseSignal.File_Upload_Failed.value
         }
        )
         
    return JSONResponse(
        content= 
        {
            "signal": ResponseSignal.File_Uploaded_Successfully.value,
            "file_id": file_id
            
         }
        )
  
    