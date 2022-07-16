from flask import Request
from conversation_assistant import run_generate_suggestions

import functions_framework  # type: ignore

from conversation_assistant.models import LambdaResponse


@functions_framework.http
def generate_suggestions(request: Request) -> LambdaResponse:
    return run_generate_suggestions(request.json)
