from unittest.mock import MagicMock, patch

from jsonschema import ValidationError

from ..lambda_helper import run_lambda
from ..models import LambdaResponse
from .mocks import MOCK_LAMBDA_EVENT, MOCK_SUGGESTIONS


@patch("conversation_assistant.lambda_helper.generate_message_suggestions", MagicMock(return_value=MOCK_SUGGESTIONS))
def test_lambda_response__when_event_is_valid__then_response_code_is_200():
    response = run_lambda(MOCK_LAMBDA_EVENT)

    assert response["statusCode"] == 200


@patch("conversation_assistant.lambda_helper.validate_message_suggestions", MagicMock(side_effect=ValidationError("test")))
def test_lambda_response__when_event_is_invalid__then_response_code_is_400():
    empty_event = {}
    response = run_lambda(empty_event)

    assert response["statusCode"] == 400


@patch(
    "conversation_assistant.lambda_helper.validate_message_suggestions",
    MagicMock(side_effect=ValidationError("'body' is a required property, and it must be a string")),
)
def test_lambda_response__when_event_is_invalid__then_returns_error_message():
    empty_event = {}
    response: LambdaResponse = run_lambda(empty_event)

    assert response["body"] == "Error - Invalid event\n" + "error='body' is a required property, and it must be a string"


@patch("conversation_assistant.lambda_helper.validate_message_suggestions", MagicMock(side_effect=RuntimeError("test")))
def test_lambda_response__when_internal_error_raised__then_response_code_is_500():

    response: LambdaResponse = run_lambda(MOCK_LAMBDA_EVENT)
    assert response["statusCode"] == 500


@patch("conversation_assistant.lambda_helper.validate_message_suggestions", MagicMock(side_effect=RuntimeError("tests")))
def test_lambda_response__when_internal_error_raised__then_returns_error_message():
    response: LambdaResponse = run_lambda(MOCK_LAMBDA_EVENT)
    assert response["body"] == "Error - Something went wrong"
