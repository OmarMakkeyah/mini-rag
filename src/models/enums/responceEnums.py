from enum import Enum

class ResponseSignal(Enum):
    
    File_Validated_Successfully = "File validated successfully"
    File_Uploaded_Successfully = "File uploaded successfully"
    
    File_Type_Not_Supported = "File type not supported"
    File_Size_Exceeded = "File size exceeded"
    File_Upload_Failed = "File upload failed"
    