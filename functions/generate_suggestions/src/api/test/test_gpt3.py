import copy
from unittest.mock import MagicMock, patch

import pytest
from jsonschema import ValidationError

from src.test.mocks.requests import EMPTY_REQUEST_WITH_NAMES

from ...models import GPT3Params
from ...test.mocks import (
    EMPTY_REQUEST,
    MOCK_GPT3_COMPLETION_RESPONSE,
    MOCK_PROMPT,
    MockMalformedResponse,
)
from ..gpt3 import fetch_completion, get_stop_indicator

MOCK_STOP_INDICATOR = ["Chad Johnson: ", "Stacey: "]
MOCK_USER_ID = "1234567890"


def test_get_stop_indicator__when_names_and_relationship_given__then_includes_them() -> None:
    request = copy.deepcopy(EMPTY_REQUEST_WITH_NAMES)
    stop_indicator = get_stop_indicator(request)
    assert stop_indicator == ["Chad Johnson:", "Stacey:"]


def test_get_stop_indicator__when_relationship_but_no_names_given__then_includes_them() -> None:
    request = copy.deepcopy(EMPTY_REQUEST)
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Professional"

    stop_indicator = get_stop_indicator(request)
    assert stop_indicator == ["Me:", "Friend:"]


def test_get_stop_indicator__when_nothing_given__then_returns_me_and_relationship() -> None:
    request = copy.deepcopy(EMPTY_REQUEST)

    stop_indicator = get_stop_indicator(request)
    assert stop_indicator == ["Me:", "Them:"]


@patch("src.gpt3.client.chat.completions.create", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
def test_fetch_completion__when_gpt3_request_succeeds__then_returns_response() -> None:
    mock_gpt3_params: GPT3Params = EMPTY_REQUEST["settings"]["gpt3_params"]

    response = fetch_completion(MOCK_PROMPT, mock_gpt3_params, MOCK_STOP_INDICATOR, MOCK_USER_ID)

    assert response == MOCK_GPT3_COMPLETION_RESPONSE.to_dict()


@patch("src.gpt3.client.chat.completions.create", MagicMock(side_effect=LookupError))
def test_fetch_completion__when_gpt3_request_fails__then_raises_error() -> None:
    mock_gpt3_params: GPT3Params = EMPTY_REQUEST["settings"]["gpt3_params"]

    with pytest.raises(LookupError):
        fetch_completion(MOCK_PROMPT, mock_gpt3_params, MOCK_STOP_INDICATOR, MOCK_USER_ID)


# Response has to be a class that has a to_dict method


@patch("src.gpt3.client.chat.completions.create", MagicMock(return_value=MockMalformedResponse()))
def test_fetch_completion__when_gpt3_request_succeeds_but_validation_fails__then_raises_validation_error() -> None:
    mock_gpt3_params: GPT3Params = EMPTY_REQUEST["settings"]["gpt3_params"]

    with pytest.raises(ValidationError):
        fetch_completion(MOCK_PROMPT, mock_gpt3_params, MOCK_STOP_INDICATOR, MOCK_USER_ID)
