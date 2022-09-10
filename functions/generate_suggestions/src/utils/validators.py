import json
import os
from typing import Any, Union

from jsonschema import validate

from ..models import GPT3CompletionResponse


def validate_request(request_body: Union[Any, None]) -> None:
    if request_body is None:
        raise ValueError("Request body is required")

    path_to_schema: str = os.path.join("schemas", "generate_suggestions_request.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(request_body, schema)


def validate_completion_response(response: GPT3CompletionResponse) -> None:
    path_to_schema: str = os.path.join("schemas", "gpt3_completion_response.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(response, schema)

def is_not_empty(field: str) -> bool:
    return len(field) > 0
