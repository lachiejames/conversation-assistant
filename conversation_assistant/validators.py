import json
import os
from typing import Any

from jsonschema import validate

from .models import GenerateMessageSuggestionsRequest, GPT3CompletionResponse


def validate_request(event: Any):
    path_to_schema: str = os.path.join("schemas", "generate_message_suggestions.json")
    generate_message_suggestions_request: GenerateMessageSuggestionsRequest = event.json

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(generate_message_suggestions_request, schema)


def validate_completion_response(response: GPT3CompletionResponse):
    path_to_schema: str = os.path.join("schemas", "gpt3_completion_response.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(response, schema)
