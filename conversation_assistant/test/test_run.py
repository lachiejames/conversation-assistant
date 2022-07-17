from unittest.mock import MagicMock, patch

from jsonschema import ValidationError

from ..run import run_generate_suggestions
from ..models import GenerateSuggestionsResponse
from .mocks import MOCK_REQUEST_BODY, MOCK_SUGGESTIONS


@patch("conversation_assistant.run.fetch_suggestions", MagicMock(return_value=MOCK_SUGGESTIONS))
def test_lambda_response__when_event_is_valid__then_response_code_is_200() -> None:
    response = run_generate_suggestions(MOCK_REQUEST_BODY)

    assert response["statusCode"] == 200


@patch("conversation_assistant.run.validate_request", MagicMock(side_effect=ValidationError("test")))
def test_lambda_response__when_event_is_invalid__then_response_code_is_400() -> None:
    empty_event: dict[str, str] = {}
    response = run_generate_suggestions(empty_event)

    assert response["statusCode"] == 400


@patch(
    "conversation_assistant.run.validate_request",
    MagicMock(side_effect=ValidationError("test")),
)
def test_lambda_response__when_event_is_invalid__then_returns_error_message() -> None:
    empty_event: dict[str, str] = {}
    response: GenerateSuggestionsResponse = run_generate_suggestions(empty_event)

    assert response["body"] == "Invalid request body: test"


@patch("conversation_assistant.run.validate_request", MagicMock(side_effect=RuntimeError("test")))
def test_lambda_response__when_internal_error_raised__then_response_code_is_500() -> None:
    response: GenerateSuggestionsResponse = run_generate_suggestions(MOCK_REQUEST_BODY)
    assert response["statusCode"] == 500


@patch("conversation_assistant.run.validate_request", MagicMock(side_effect=RuntimeError("test")))
def test_lambda_response__when_internal_error_raised__then_returns_error_message() -> None:
    response: GenerateSuggestionsResponse = run_generate_suggestions(MOCK_REQUEST_BODY)
    assert response["body"] == "Something went wrong: test"
