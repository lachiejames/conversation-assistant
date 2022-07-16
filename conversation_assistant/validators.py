import json
import os
from typing import Any

from jsonschema import ValidationError, validate

from .models import (
    GenerateMessageSuggestionsRequest,
    GPT3CompletionResponse,
    LambdaEvent,
)


def validate_message_suggestions(event: LambdaEvent):
    path_to_schema: str = os.path.join("schemas", "generate_message_suggestions.json")
    generate_message_suggestions_request: GenerateMessageSuggestionsRequest = json.loads(event["body"])

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(generate_message_suggestions_request, schema)


def validate_completion_response(response: GPT3CompletionResponse):
    path_to_schema: str = os.path.join("schemas", "gpt3_completion_response.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(response, schema)
