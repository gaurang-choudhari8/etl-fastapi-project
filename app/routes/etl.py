from typing import Annotated
from fastapi import APIRouter, File, UploadFile, HTTPException

router = APIRouter()


@router.post("/upload/")
async def upload_file(file: UploadFile | None = None):
    if not file:
        return {"error": "No file uploaded"}
    
    extn = file.filename.split(".")[-1].lower()
    if extn not in ["csv"]:
        raise HTTPException("Only CSV files are allowed")

