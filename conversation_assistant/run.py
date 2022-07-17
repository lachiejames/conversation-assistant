import json
from typing import Any, Union

from jsonschema import ValidationError

from .generator import fetch_suggestions
from .models import GenerateSuggestionsRequest, GenerateSuggestionsResponse, Suggestion
from .validators import validate_request


HEADERS = {
    "Content-Type": "application/json",
}


def respond_with_200(request: GenerateSuggestionsRequest) -> GenerateSuggestionsResponse:
    suggestions: list[Suggestion] = fetch_suggestions(request)

    return (json.dumps({"results": suggestions}), 200, HEADERS)


def respond_with_400(error: ValidationError) -> GenerateSuggestionsResponse:
    return (f"Invalid request body: {error.message}", 400, HEADERS)


def respond_with_500(error: Exception) -> GenerateSuggestionsResponse:
    return (f"Something went wrong: {error}", 500, HEADERS)


# request_body typed as 'Any' until after validate_request(request_body)
def run_generate_suggestions(request_body: Union[Any, None]) -> GenerateSuggestionsResponse:
    try:
        try:
            if request_body is None:
                raise ValueError("Request body is required")
            validate_request(request_body)
            return respond_with_200(request_body)

        except ValueError as error:
            return respond_with_400(error)

        except ValidationError as error:
            return respond_with_400(error)

    except Exception as error:
        return respond_with_500(error)
