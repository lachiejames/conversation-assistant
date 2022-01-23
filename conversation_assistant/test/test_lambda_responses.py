from conversation_assistant.lambda_responses import lambda_response
from conversation_assistant.models import LambdaResponse
from conversation_assistant.test.mocks import MOCK_LAMBDA_EVENT


def test_lambda_response__when_event_is_valid__then_response_code_is_200():
    response = lambda_response(MOCK_LAMBDA_EVENT)

    assert response["statusCode"] == 200


def test_lambda_response__when_event_is_valid__then_returns_at_least_1_message_suggestion():
    response: LambdaResponse = lambda_response(MOCK_LAMBDA_EVENT)

    assert len(response["body"]["results"]) > 0
