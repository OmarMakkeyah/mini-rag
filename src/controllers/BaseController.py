from helpers.config import get_settings
from fastapi import UploadFile
import os
import string
import random
import time

class BaseController:
    
    def __init__(self):
        self.settings = get_settings()
       
        self.basePath = os.path.dirname(os.path.dirname(__file__))
        self.filesPath = os.path.join(self.basePath,"assets/files")
    
    def generate_random_string_with_time(self):
        randString = "".join(random.choices(string.ascii_lowercase + string.digits, k= 6))
        timeString = str(int(time.time()*1000))
        return f"{randString}_{timeString}"
    
   
        
        