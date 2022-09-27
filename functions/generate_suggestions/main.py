from typing import Any, Union

import functions_framework
from flask import Request, Response

from src import run_generate_suggestions


@functions_framework.http
def generate_suggestions(request: Request) -> Response:
    return run_generate_suggestions(request)
