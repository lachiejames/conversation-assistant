from unittest.mock import MagicMock, patch

from flask import Response
from jsonschema import ValidationError

from ..run import run_generate_suggestions
from .mocks import MOCK_REQUEST_BODY, MOCK_RESPONSE, MOCK_SUGGESTIONS


@patch("conversation_assistant.run.fetch_suggestions", MagicMock(return_value=MOCK_SUGGESTIONS))
def test_run_generate_suggestions__when_event_is_valid__then_response_code_is_200() -> None:
    response = run_generate_suggestions(MOCK_REQUEST_BODY)

    assert response.status_code == 200


@patch("conversation_assistant.run.fetch_suggestions", MagicMock(return_value=MOCK_SUGGESTIONS))
def test_run_generate_suggestions__when_event_is_valid__then_returns_results() -> None:
    response = run_generate_suggestions(MOCK_REQUEST_BODY)

    assert response.data == MOCK_RESPONSE


@patch("conversation_assistant.run.validate_request", MagicMock(side_effect=ValidationError("test")))
def test_run_generate_suggestions__when_event_is_invalid__then_response_code_is_400() -> None:
    empty_event: dict[str, str] = {}
    response = run_generate_suggestions(empty_event)

    assert response.status_code == 400


@patch(
    "conversation_assistant.run.validate_request",
    MagicMock(side_effect=ValidationError("test")),
)
def test_run_generate_suggestions__when_event_is_invalid__then_returns_error_message() -> None:
    empty_event: dict[str, str] = {}
    response: Response = run_generate_suggestions(empty_event)

    assert response.data == b"Invalid request body: test"


@patch("conversation_assistant.run.validate_request", MagicMock(side_effect=RuntimeError("test")))
def test_run_generate_suggestions__when_internal_error_raised__then_response_code_is_500() -> None:
    response: Response = run_generate_suggestions(MOCK_REQUEST_BODY)
    assert response.status_code == 500


@patch("conversation_assistant.run.validate_request", MagicMock(side_effect=RuntimeError("test")))
def test_run_generate_suggestions__when_internal_error_raised__then_returns_error_message() -> None:
    response: Response = run_generate_suggestions(MOCK_REQUEST_BODY)
    assert response.data == b"Something went wrong: test"
