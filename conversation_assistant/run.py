import json
from typing import Any, Union

from flask import Response
from jsonschema import ValidationError

from .generator import fetch_suggestions
from .models import GenerateSuggestionsRequest, GenerateSuggestionsResponse, Suggestion
from .validators import validate_request

HEADERS = {
    "Content-Type": "application/json",
}


def respond_with_200(request: GenerateSuggestionsRequest) -> Response:
    suggestions: list[Suggestion] = fetch_suggestions(request)
    response: GenerateSuggestionsResponse = {"results": suggestions}

    return Response(
        response=json.dumps(response),
        status=200,
        headers=HEADERS,
    )


def respond_with_400(error: Exception) -> Response:
    return Response(
        response=f"Invalid request body: {error}",
        status=400,
        headers=HEADERS,
    )


def respond_with_500(error: Exception) -> Response:
    return Response(
        response=f"Something went wrong: {error}",
        status=500,
        headers=HEADERS,
    )


# request_body typed as 'Any' until after validate_request(request_body)
def run_generate_suggestions(request_body: Union[Any, None]) -> Response:
    try:
        try:
            validate_request(request_body)
            return respond_with_200(request_body)

        except (ValueError, ValidationError) as error:
            return respond_with_400(error)

    except Exception as error:
        return respond_with_500(error)
