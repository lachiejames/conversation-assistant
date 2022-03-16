from unittest.mock import MagicMock, patch
from jsonschema import ValidationError

import pytest

from conversation_assistant.models.gpt3_params import GPT3Params

from ..gpt3 import fetch_completion
from .mocks import MOCK_GPT3_COMPLETION_RESPONSE, MOCK_PROMPT, MOCK_REQUEST


@patch("conversation_assistant.gpt3.Completion.create", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
def test_fetch_completion__when_gpt3_request_succeeds__then_returns_response():
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["gpt3_params"]

    response = fetch_completion(MOCK_PROMPT, mock_gpt3_params)

    assert response is MOCK_GPT3_COMPLETION_RESPONSE


@patch("conversation_assistant.gpt3.Completion.create", MagicMock(side_effect=LookupError))
def test_fetch_completion__when_gpt3_request_fails__then_raises_error():
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["gpt3_params"]

    with pytest.raises(LookupError):
        fetch_completion(MOCK_PROMPT, mock_gpt3_params)


@patch("conversation_assistant.gpt3.Completion.create", MagicMock(return_value={"this": "will fail"}))
def test_fetch_completion__when_gpt3_request_succeeds_but_validation_fails__then_raises_validation_error():
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["gpt3_params"]

    with pytest.raises(ValidationError):
        fetch_completion(MOCK_PROMPT, mock_gpt3_params)
