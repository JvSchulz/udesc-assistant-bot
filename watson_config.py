from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException
import os
from dotenv import load_dotenv
import json

load_dotenv()

authenticator = IAMAuthenticator(os.getenv("WATSON_ASSISTANT_API_KEY"))
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)


assistant.set_service_url(os.getenv("SERVICE_INSTANCE_URL"))

response = assistant.message_stateless(
    assistant_id=os.getenv("WATSON_ASSISTANT_ID"),
    environment_id=os.getenv("ENVIRONMENT_ID"),
    input={
        'message_type': 'text',
        'text': 'Centros'
    },
    user_id= "teste"
).get_result()

print(json.dumps(response, indent=2))

# try:
    # # Invoke a method
    # except ApiException as ex:
    # print "Method failed with status code " + str(ex.code) + ": " + ex.message