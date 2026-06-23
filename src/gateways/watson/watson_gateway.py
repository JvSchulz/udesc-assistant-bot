from src.gateways.watson import watson_config
import json

class WatsonGateway:
    def __init__(self):
        self.assistant = watson_config.load_assistant()
        self.assistant_id = watson_config.assistant_id
        self.environment_id = watson_config.environment_id
        
    def test_assistant(self):
        assistant = self.assistant
        response = assistant.message_stateless(
            assistant_id=self.assistant_id,
            environment_id=self.environment_id,
            input={
                'message_type': 'text',
                'text': 'Centros'
            },
            user_id= "teste" #obrigatorio um id para usuário, ciar um UUID vindo do dos gateways
        ).get_result()
        print(json.dumps(response, indent=2))

