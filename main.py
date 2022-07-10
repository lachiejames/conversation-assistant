from dotenv import load_dotenv

from conversation_assistant import LambdaEvent, run_lambda


def generate_suggestions(request: LambdaEvent):
    load_dotenv(".env")
    return run_lambda(request)
