from typing import Annotated
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from services.s3_service import s3_service_class

router = APIRouter()


@router.post("/upload")
async def upload_file(s3_client: Annotated[s3_service_class,Depends(s3_service_class)], file: UploadFile | None = None, key: str | None = None, bucket_name: str | None = None):
    #If there is no file, then return error no file uploaded 
    if not file:
        raise HTTPException(status_code = 400, detail = {"error": "No file uploaded"})
    
    #If improper extension, then raise HTTP Error
    extn = file.filename.split(".")[-1].lower()
    if extn not in ["csv","txt"]:
        raise HTTPException(status_code = 400, detail = "Only CSV or Text files are allowed")

    #Call the service method to upload file
    try:
        s3_client.upload_file(file, key, bucket_name)
        return {
            "status": "Success",
            "message": "File uploaded successfully",
            "bucket": str(bucket_name),
            "key": str(key)
        }
    except Exception as exp:
        raise HTTPException(status_code=500, detail = {
            "status": "Failed",
            "description": str(exp)
        })



