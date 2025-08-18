from fastapi import FastAPI
from routes import etl
app = FastAPI()


@app.get("/")
async def test():
    return {"message": "Hello World"}