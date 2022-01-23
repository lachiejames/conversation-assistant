from dotenv import load_dotenv

from conversation_assistant.lambda_responses import lambda_response
from conversation_assistant.models import LambdaRequest


def lambda_handler(request: LambdaRequest):
    print(f"request = {request}")

    load_dotenv(".env")

    return lambda_response(request)
