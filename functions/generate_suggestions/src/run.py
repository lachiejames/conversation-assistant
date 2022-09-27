import json
from typing import Any, Union, cast

from flask import Response
from jsonschema import ValidationError

from .api import generate_suggestions
from .models import GenerateSuggestionsRequest, GenerateSuggestionsResponse
from .utils import validate_request
from .stream_identify import main
HEADERS = {
    "Content-Type": "application/json",
}


def respond_with_200(request: GenerateSuggestionsRequest) -> Response:
    response: GenerateSuggestionsResponse = generate_suggestions(request)

    return Response(
        response=json.dumps(response),
        status=200,
        headers=HEADERS,
    )


def respond_with_400(e: Exception) -> Response:
    print(f"400 - {e}")
    return Response(
        response=str(e),
        status=400,
        headers=HEADERS,
    )


def respond_with_500(e: Exception) -> Response:
    print(f"500 - {e}")
    return Response(
        response=str(e),
        status=500,
        headers=HEADERS,
    )


# request_body typed as 'Any' until after validate_request(request_body)
def run_generate_suggestions(request_body: Union[Any, None]) -> Response:
    main()
    # try:
    #     try:
    #         validate_request(request_body)

    #         # If we reach this point, the request must be of type 'GenerateSuggestionsRequest'
    #         request_body = cast(GenerateSuggestionsRequest, request_body)
    #         return respond_with_200(request_body)

    #     except (ValueError, ValidationError) as e:
    #         return respond_with_400(e)

    # # Used to catch any exception that is not caught by the above try block
    # # pylint: disable=broad-except
    # except Exception as e:
    #     return respond_with_500(e)
