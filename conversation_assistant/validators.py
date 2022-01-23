import json
import os
from typing import Any

from jsonschema import validate

from conversation_assistant.models.lambda_event import LambdaEvent


def validate_message_suggestions(event: LambdaEvent):
    path_to_schema: str = os.path.join("schemas", "generate-message-suggestions.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(event, schema)
