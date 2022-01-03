import json

from dotenv import load_dotenv

from conversation_assistant.generator import generate_message_suggestions
from conversation_assistant.models import LambdaEvent, Suggestion


def lambda_handler(event: LambdaEvent, context):
    load_dotenv(".env")

    suggestions: list[Suggestion] = generate_message_suggestions(event)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"results": suggestions}),
    }
