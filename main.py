from fastapi import FastAPI
from src.gateways.watson import watson_gateway

app = FastAPI()

watson_gateway.test_assistant()

@app.get("/")
async def root():
    return {"message": "Hello World"} teste