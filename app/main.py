from fastapi import FastAPI
from routes import etl
app = FastAPI()
app.include_router(etl.router)

@app.get("/")
async def test():
    return {"message": "Hello World"}