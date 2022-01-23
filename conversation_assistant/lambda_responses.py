import json

from jsonschema import ValidationError

from conversation_assistant.generator import generate_message_suggestions
from conversation_assistant.models import LambdaResponse, LambdaEvent, Suggestion
from conversation_assistant.validators import validate_message_suggestions


def respond_with_200(event: LambdaEvent) -> LambdaResponse:
    suggestions: list[Suggestion] = generate_message_suggestions(event)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": {"results": suggestions},
    }


def respond_with_400(event: LambdaEvent) -> LambdaResponse:
    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"error": f"Invalid request - event={event}"}),
    }


def respond_with_500(event: LambdaEvent) -> LambdaResponse:
    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"error": f"Something went wrong... event={event}"}),
    }


def lambda_response(event: LambdaEvent) -> LambdaResponse:
    try:
        validate_message_suggestions(event)
        return respond_with_200(event)

    except ValidationError:
        return respond_with_400(event)

    return respond_with_500(event)
