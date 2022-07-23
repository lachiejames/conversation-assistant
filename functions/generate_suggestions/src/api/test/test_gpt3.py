from unittest.mock import MagicMock, patch

import pytest
from jsonschema import ValidationError

from ...models import GPT3Params
from ...test.mocks import MOCK_GPT3_COMPLETION_RESPONSE, MOCK_PROMPT, MOCK_REQUEST
from ..gpt3 import fetch_completion, get_stop_indicator

MOCK_STOP_INDICATOR = ["Chad Johnson: ", "Stacey: "]


def test_get_stop_indicator__returns_2_indicators() -> None:
    stop_indicator = get_stop_indicator(request=MOCK_REQUEST)

    assert len(stop_indicator) == 2


@patch("src.gpt3.Completion.create", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
def test_fetch_completion__when_gpt3_request_succeeds__then_returns_response() -> None:
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["settings"]["gpt3_params"]

    response = fetch_completion(MOCK_PROMPT, mock_gpt3_params, MOCK_STOP_INDICATOR)

    assert response == MOCK_GPT3_COMPLETION_RESPONSE


@patch("src.gpt3.Completion.create", MagicMock(side_effect=LookupError))
def test_fetch_completion__when_gpt3_request_fails__then_raises_error() -> None:
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["settings"]["gpt3_params"]

    with pytest.raises(LookupError):
        fetch_completion(MOCK_PROMPT, mock_gpt3_params, MOCK_STOP_INDICATOR)


@patch("src.gpt3.Completion.create", MagicMock(return_value={"this": "will fail"}))
def test_fetch_completion__when_gpt3_request_succeeds_but_validation_fails__then_raises_validation_error() -> None:
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["settings"]["gpt3_params"]

    with pytest.raises(ValidationError):
        fetch_completion(MOCK_PROMPT, mock_gpt3_params, MOCK_STOP_INDICATOR)
