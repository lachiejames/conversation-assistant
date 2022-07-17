from typing import Any, Union
from flask import Request

from conversation_assistant import run_generate_suggestions, GenerateSuggestionsResponse


def generate_suggestions(request: Request) -> GenerateSuggestionsResponse:
    request_body: Union[Any, None] = request.get_json(silent=True)
    return run_generate_suggestions(request_body)
