import json
import os
from typing import Any, Union

from jsonschema import validate

from ..models import GenerateSuggestionsRequest, GPT3CompletionResponse


def get_path_to_schema(schema_name: str) -> str:
    return os.path.abspath(
        os.path.join(
            __file__,
            "..",
            "..",
            "..",
            "schemas",
            schema_name,
        )
    )


def validate_request(request_body: Union[Any, None]) -> None:
    if request_body is None:
        raise ValueError("Request body is required")

    path_to_schema: str = get_path_to_schema("generate_suggestions_request.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(request_body, schema)


def validate_completion_response(response: GPT3CompletionResponse) -> None:
    path_to_schema: str = get_path_to_schema("gpt3_completion_response.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(response, schema)


def is_not_empty(field: str) -> bool:
    return len(field) > 0


def choose_path_prefix(request: GenerateSuggestionsRequest) -> str:
    my_name = request["settings"]["profile_params"]["name"]
    their_name = request["settings"]["conversation_params"]["their_name"]
    has_names = is_not_empty(my_name) and is_not_empty(their_name)

    if has_names:
        return "names"
    return "no_names"
