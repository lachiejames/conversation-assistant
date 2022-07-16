from flask import Request
from conversation_assistant import run_generate_suggestions

import functions_framework  # type: ignore

from conversation_assistant.models import GenerateSuggestionsResponse


@functions_framework.http
def generate_suggestions(request: Request) -> GenerateSuggestionsResponse:
    return run_generate_suggestions(request.get_json(silent=True))
