import json

from jsonschema import ValidationError

from .generator import generate_message_suggestions
from .models import (
    GenerateMessageSuggestionsRequest,
    LambdaEvent,
    LambdaResponse,
    Suggestion,
)
from .validators import validate_message_suggestions


def respond_with_200(request: GenerateMessageSuggestionsRequest) -> LambdaResponse:
    suggestions: list[Suggestion] = generate_message_suggestions(request)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"results": suggestions}),
    }


def respond_with_400(error: ValidationError) -> LambdaResponse:
    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": f"Error - Invalid event\nerror={error.message}",
    }


def respond_with_500(error: Exception) -> LambdaResponse:
    print(error)

    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": "Error - Something went wrong",
    }


def lambda_response(event: LambdaEvent) -> LambdaResponse:
    try:
        try:
            validate_message_suggestions(event)
            request: GenerateMessageSuggestionsRequest = json.loads(event["body"])
            return respond_with_200(request)

        except ValidationError as error:
            return respond_with_400(error)

    except Exception as error:
        return respond_with_500(error)
