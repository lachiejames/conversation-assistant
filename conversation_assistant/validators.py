import json
import os
from typing import Any

from jsonschema import validate


def validate_message_suggestions(obj: Any):
    path_to_schema: str = os.path.join("schemas", "generate-message-suggestions.json")

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(obj, schema)
