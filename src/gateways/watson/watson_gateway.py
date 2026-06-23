from src.gateways.watson import watson_config
import json

def test_assistant():
    assistant = watson_config.load_assistant()
    response = assistant.message_stateless(
        assistant_id=watson_config.assistant_id,
        environment_id=watson_config.environment_id,
        input={
            'message_type': 'text',
            'text': 'Centros'
        },
        user_id= "teste" #obrigatorio um id para usuário, ciar um UUID vindo do dos gateways
    ).get_result()
    print(json.dumps(response, indent=2))

