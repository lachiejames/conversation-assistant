from typing import Any

from dotenv import load_dotenv

from conversation_assistant import LambdaEvent, lambda_response


def lambda_handler(event: LambdaEvent, _: Any):
    print(f"event = {event}")

    load_dotenv(".env")

    return lambda_response(event)
