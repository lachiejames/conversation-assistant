import json
from typing import Any, Union

from jsonschema import ValidationError

from .generator import fetch_suggestions
from .models import GenerateSuggestionsRequest, LambdaResponse, Suggestion
from .validators import validate_request


def respond_with_200(request: GenerateSuggestionsRequest) -> LambdaResponse:
    suggestions: list[Suggestion] = fetch_suggestions(request)

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
        "body": f"Invalid request body: {error.message}",
    }


def respond_with_500(error: Exception) -> LambdaResponse:
    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": f"Something went wrong: {error}",
    }


# request_body typed as 'Any' until after validate_request(request_body)
def run_generate_suggestions(request_body: Union[Any, None]) -> LambdaResponse:
    try:
        try:
            assert request_body is not None
            validate_request(request_body)
            return respond_with_200(request_body)

        except ValidationError as error:
            return respond_with_400(error)

    except Exception as error:
        return respond_with_500(error)
