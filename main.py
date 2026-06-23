from fastapi import FastAPI
from src.gateways.watson.watson_gateway import WatsonGateway

app = FastAPI()

watson_gateway = WatsonGateway()
watson_gateway.test_assistant()

@app.get("/")
async def root():
    return {"message": "Hello World"} 
