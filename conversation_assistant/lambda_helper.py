import json
from typing import Any

from jsonschema import ValidationError

from .generator import generate_message_suggestions
from .models import GenerateMessageSuggestionsRequest, LambdaResponse, Suggestion
from .validators import validate_request


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
        "body": f"Error - Invalid request\nerror={error.message}",
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


# request_body typed as 'Any' until after validate_request(request_body)
def run_generate_suggestions(request_body: Any) -> LambdaResponse:
    try:
        try:
            validate_request(request_body)
            return respond_with_200(request_body)

        except ValidationError as error:
            return respond_with_400(error)

    except Exception as error:
        return respond_with_500(error)
