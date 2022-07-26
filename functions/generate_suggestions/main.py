from typing import Any, Union

from flask import Request, Response

from src import run_generate_suggestions

import functions_framework

@functions_framework.http
def generate_suggestions(request: Request) -> Response:
    request_body: Union[Any, None] = request.get_json(silent=True)
    return run_generate_suggestions(request_body)
