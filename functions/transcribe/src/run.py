import json
from typing import Any, Union, cast

from flask import Response

from .models import TranscribeRequest, TranscribeResponse
from .transcribe import transcribe_data

HEADERS = {
    "Content-Type": "application/json",
}


def respond_with_200(audio_data: str) -> Response:
    response: TranscribeResponse = transcribe_data(audio_data)

    return Response(
        response=json.dumps(response),
        status=200,
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
def run_transcribe(request_body: Union[Any, None]) -> Response:
    try:
        # TODO: add validation

        request_body = cast(TranscribeRequest, request_body)
        return respond_with_200(request_body)

    # Used to catch any exception that is not caught by the above try block
    # pylint: disable=broad-except
    except Exception as e:
        return respond_with_500(e)
