from .BaseController import BaseController
import os

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()
        
    def get_project_path(self,project_id:str):
        projectPath = os.path.join(self.filesPath,project_id)
        
        if not os.path.exists(projectPath):
            os.makedirs(projectPath)
        
        return projectPath
        
        