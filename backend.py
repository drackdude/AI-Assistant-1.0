# backend.py

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import shutil



app = FastAPI()


class Audio(BaseModel):
    filename: str
    content_type: str
    file_size: int

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Calculate file size
    file.file.seek(0, 2)  # Move the pointer to the end of the file
    file_size = file.file.tell()  # Get the current position of the pointer (which is the file size)
    
    return {"filename": file.filename, "content_type": file.content_type, "file_size": file_size}
