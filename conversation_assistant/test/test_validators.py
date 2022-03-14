import json
from typing import Any

import pytest
from jsonschema import ValidationError

from ..models import LambdaEvent
from ..validators import validate_message_suggestions


def test_validate_message_suggestions__when_event_is_valid__then_succeeds():
    valid_event: LambdaEvent = {
        "body": json.dumps(
            {
                "previous_messages": [
                    {
                        "text": "Oi mate",
                        "author": "Ben Kerr",
                    },
                    {
                        "text": "Yo dude",
                        "author": "Me",
                    },
                ],
                "gpt3_params": {
                    "randomness": 0.7,
                    "num_results": 3,
                    "max_length": 50,
                },
            }
        )
    }

    validate_message_suggestions(valid_event)


def test_validate_message_suggestions__when_event_is_valid_and_previous_messages_empty__then_succeeds():
    valid_event: LambdaEvent = {
        "body": json.dumps(
            {
                "previous_messages": [],
                "gpt3_params": {
                    "randomness": 0.7,
                    "num_results": 3,
                    "max_length": 50,
                },
            }
        )
    }

    validate_message_suggestions(valid_event)


def test_validate_message_suggestions__when_event_body_is_an_object_instead_of_a_string__then_raises_validation_error():
    invalid_event: Any = {
        "body": {
            "previous_messages": [],
            "gpt3_params": {
                "randomness": 0.7,
                "num_results": 3,
                "max_length": 50,
            },
        }
    }

    with pytest.raises(ValidationError):
        validate_message_suggestions(invalid_event)


def test_validate_message_suggestions__when_event_not_wrapped_in_body__then_raises_validation_error():
    invalid_event: Any = json.dumps(
        {
            "previous_messages": [
                {
                    "text": "Oi mate",
                    "author": "Ben Kerr",
                },
                {
                    "text": "Yo dude",
                    "author": "Me",
                },
            ],
            "gpt3_params": {
                "randomness": 0.7,
                "num_results": 3,
                "max_length": 50,
            },
        }
    )

    with pytest.raises(ValidationError):
        validate_message_suggestions(invalid_event)


def test_validate_message_suggestions__when_event_is_empty__then_raises_validation_error():
    invalid_event: Any = {"body": json.dumps({})}

    with pytest.raises(ValidationError):
        validate_message_suggestions(invalid_event)
