import json
import os
from typing import Any

from jsonschema import ValidationError, validate

from conversation_assistant.models import GenerateMessageSuggestionsRequest, LambdaEvent


def validate_message_suggestions(event: LambdaEvent):
    try:
        json.loads(event["body"])
    except Exception as error:
        raise ValidationError("'body' is a required property") from error

    path_to_schema: str = os.path.join("schemas", "generate-message-suggestions.json")
    generate_message_suggestions_request: GenerateMessageSuggestionsRequest = json.loads(event["body"])

    with open(path_to_schema, "r", encoding="utf-8") as schema_file:
        schema: Any = json.load(schema_file)
        validate(generate_message_suggestions_request, schema)
