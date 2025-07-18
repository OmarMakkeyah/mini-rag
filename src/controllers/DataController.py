from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re 
import os
import string


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 #convert MB to Bytes
        
    def validate_uploaded_file(self,file: UploadFile):
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.File_Type_Not_Supported.value
        
        if file.size > self.settings.FILE_MAX_SIZE*self.size_scale:
            return False, ResponseSignal.File_Size_Exceeded.value
        
        return True, ResponseSignal.File_Validated_Successfully.value
    
    def get_cleaned_filename(self, orig_filename:str):
       return re.sub(r"[^a-zA-Z0-9._]","",orig_filename)
   
    def generate_unique_file_Path(self, project_id: str, orig_filename:str):
        projectPath = ProjectController().get_project_path(project_id=project_id)
        cleaned_file_name = self.get_cleaned_filename(orig_filename= orig_filename)
        key = self.generate_random_string_with_time()
        filePath = os.path.join(projectPath,f"{key}_{cleaned_file_name}")   
        while os.path.exists(filePath):
            key = self.generate_random_string_with_time()
            full_filename = f"{key}_{cleaned_file_name}"
            filePath = os.path.join(projectPath, full_filename)
        return filePath, key
  
                             
                