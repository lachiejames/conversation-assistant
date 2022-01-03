import json
from dotenv import load_dotenv
from conversation_assistant.generator import generate_message_suggestions
from conversation_assistant.models import Message, Suggestion


def lambda_handler(event, context):
    load_dotenv(".env")

    previous_messages: list[Message] = event["previous_messages"]
    suggestions: list[Suggestion] = generate_message_suggestions(previous_messages)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"results": suggestions}),
    }
