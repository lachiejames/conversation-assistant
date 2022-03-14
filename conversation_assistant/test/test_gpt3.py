from unittest.mock import MagicMock, patch


from conversation_assistant.models.gpt3_params import GPT3Params

from ..gpt3 import fetch_completion
from .mocks import MOCK_PROMPT, MOCK_REQUEST


@patch("conversation_assistant.gpt3.Completion.create")
def test_fetch_completion__when_all_gpt3_params_passed__then_each_param_mapped_to_api_param(create_completion_spy: MagicMock):
    mock_gpt3_params: GPT3Params = MOCK_REQUEST["gpt3_params"]

    fetch_completion(MOCK_PROMPT, mock_gpt3_params)

    call_dict = create_completion_spy.call_args_list[0][1]

    assert call_dict["prompt"] is MOCK_PROMPT
    assert call_dict["api_key"] is mock_gpt3_params["api_key"]
    assert call_dict["n"] is mock_gpt3_params["n"]
    assert call_dict["temperature"] is mock_gpt3_params["temperature"]
    assert call_dict["max_tokens"] is mock_gpt3_params["max_tokens"]
    assert call_dict["top_p"] is mock_gpt3_params["top_p"]
    assert call_dict["best_of"] is mock_gpt3_params["best_of"]
    assert call_dict["frequency_penalty"] is mock_gpt3_params["frequency_penalty"]
    assert call_dict["presence_penalty"] is mock_gpt3_params["presence_penalty"]
    assert call_dict["stop"] is mock_gpt3_params["stop"]
