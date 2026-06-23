from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import os
from dotenv import load_dotenv

load_dotenv()
assistant_id=os.getenv("WATSON_ASSISTANT_ID")
environment_id=os.getenv("ENVIRONMENT_ID")
assistant_api_key=os.getenv("WATSON_ASSISTANT_API_KEY")
service_url=os.getenv("SERVICE_INSTANCE_URL")

def load_assistant() -> AssistantV2:
    
    authenticator = IAMAuthenticator(assistant_api_key)
    assistant = AssistantV2(version="2021-11-27", authenticator=authenticator)
    assistant.set_service_url(service_url)
    return assistant