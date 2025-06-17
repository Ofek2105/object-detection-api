from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from .detection import detect_objects
import shutil
import uuid
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {"message": "Object Detection API is running."}


@app.post("/detect/")
async def detect(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = detect_objects(file_path)
    return JSONResponse(content={"file": file.filename, "detections": results})
