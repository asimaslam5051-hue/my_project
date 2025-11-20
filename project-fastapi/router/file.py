from fastapi import HTTPException,File,APIRouter,UploadFile
import os
import shutil
from fastapi.responses import FileResponse

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/file")
def get_file(file: bytes = File(...)):
    try:
        content = file.decode("utf-8")
        lines = content.split("\n")
        return {"lines": lines}
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File is not a UTF-8 text file")
UPLOAD_DIR = "files"
os.makedirs(UPLOAD_DIR, exist_ok=True) 

@router.post("/uploadfile")
def get_uploadfile(upload_file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, upload_file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        "filename": path,
        "type": upload_file.content_type
    }

@router.get('/download({name})',response_class = FileResponse)
def get_file(name:str):
    file_path = os.path.join(UPLOAD_DIR, name)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path)