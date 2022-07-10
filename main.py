from typing import Any

from dotenv import load_dotenv

from conversation_assistant import LambdaEvent, run_lambda


def lambda_handler(event: LambdaEvent, _: Any):
    print(f"event = {event}")

    load_dotenv(".env")

    return run_lambda(event)
