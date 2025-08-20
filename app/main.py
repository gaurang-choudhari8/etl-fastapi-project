from fastapi import FastAPI
from routes import etl
app = FastAPI()
app.include_router(etl.router, prefix ="/s3_operations")

@app.get("/")
async def test():
    return {"message": "Hello World"}