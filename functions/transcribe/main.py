from typing import Any, Union

import functions_framework
from flask import Request, Response

from src import run_transcribe


@functions_framework.http
def transcribe(request: Request) -> Response:
    request_body: Union[Any, None] = request.get_json(silent=True)
    return run_transcribe(request_body)
