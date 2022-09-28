import functions_framework
from flask import Request, Response

from src import run_transcribe


@functions_framework.http
def transcribe(request: Request) -> Response:
    return run_transcribe(request.data)
