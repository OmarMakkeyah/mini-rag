from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 #convert MB to Bytes
        
    def validate_uploaded_file(self,file: UploadFile):
        if file.content_type not in self.settings.File_Allowed_Types:
            return False, ResponseSignal.File_Type_Not_Supported.value
        
        if file.size > self.settings.File_Max_Size*self.size_scale:
            return False, ResponseSignal.File_Size_Exceeded.value
        
        return True, ResponseSignal.File_Validated_Successfully.value