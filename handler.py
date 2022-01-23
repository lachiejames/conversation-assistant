from dotenv import load_dotenv

from conversation_assistant.lambda_responses import lambda_response
from conversation_assistant.models import LambdaEvent


def lambda_handler(event: LambdaEvent):
    print(f"event = {event}")

    load_dotenv(".env")

    return lambda_response(event)
