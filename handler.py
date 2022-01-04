import json
from logging import log

from dotenv import load_dotenv

from conversation_assistant.generator import generate_message_suggestions
from conversation_assistant.models import LambdaEvent, Suggestion
from conversation_assistant.models import lambda_event
from conversation_assistant.models.lambda_event import LambdaRequest


def respond_with_200(event: LambdaEvent):
    print(f"The event is valid.  Generating message suggestions...")
    suggestions: list[Suggestion] = generate_message_suggestions(event)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"results": suggestions}),
    }


def respond_with_400(event: LambdaEvent):
    print(f"The event is NOT valid, responding with error")

    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"error": f"Invalid request body - {event}"}),
    }


def respond_with_500(request: LambdaRequest):
    print(f"The event is NOT valid, responding with error")

    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"error": f"Invalid request - {request}"}),
    }


def lambda_handler(request: LambdaRequest, context):
    print(f"request = {request}\n\ncontext = {context}")

    load_dotenv(".env")

    if "body" in request:
        lambda_event: LambdaEvent = json.loads(request["body"])

        if "previous_messages" in lambda_event and "gpt3_params" in lambda_event:
            return respond_with_200(lambda_event)
        return respond_with_400(lambda_event)

    return respond_with_500(request)
