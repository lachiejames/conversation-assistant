import json
from typing import Any

import pytest
from jsonschema import ValidationError

from ..models import LambdaEvent
from ..validators import validate_completion_response, validate_message_suggestions
from .mocks import MOCK_GPT3_COMPLETION_RESPONSE, MOCK_REQUEST


def test_validate_message_suggestions__when_event_is_valid__then_succeeds():
    valid_event: LambdaEvent = {"body": json.dumps(MOCK_REQUEST)}

    validate_message_suggestions(valid_event)


def test_validate_message_suggestions__when_event_body_is_an_object_instead_of_a_string__then_raises_validation_error():
    invalid_event: Any = {"body": MOCK_REQUEST}

    with pytest.raises(ValidationError):
        validate_message_suggestions(invalid_event)


def test_validate_message_suggestions__when_event_not_wrapped_in_body__then_raises_validation_error():
    invalid_event: Any = MOCK_REQUEST

    with pytest.raises(ValidationError):
        validate_message_suggestions(invalid_event)


def test_validate_message_suggestions__when_event_is_empty__then_raises_validation_error():
    invalid_event: Any = {"body": json.dumps({})}

    with pytest.raises(ValidationError):
        validate_message_suggestions(invalid_event)


def test_validate_completion_response__when_event_is_valid__then_succeeds():
    validate_completion_response(MOCK_GPT3_COMPLETION_RESPONSE)


def test_validate_completion_response__when_event_is_invalid__then_raises_validation_error():
    invalid_event: Any = {"this": "will fail"}

    with pytest.raises(ValidationError):
        validate_completion_response(invalid_event)
