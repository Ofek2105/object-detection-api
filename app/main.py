"""
This file is for serving an HTML
and handle object detection requests for images
"""
import shutil
import uuid
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from .detection import detect_objects

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    """
    Currently a filler,
    In the future it will provide the HTML website
    """
    return {"message": "Object Detection API is running."}


@app.post("/detect/")
async def detect(file: UploadFile = File(...)):
    """
    function that will activate object detection on the input
    :param file: a File
    :return: Json of the detected objects
    """
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = detect_objects(file_path)
    return JSONResponse(content={"file": file.filename, "detections": results})
