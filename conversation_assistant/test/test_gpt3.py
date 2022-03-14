from unittest.mock import MagicMock, patch

from openai import Completion
from conversation_assistant.models.gpt3_params import GPT3Params
from ..gpt3 import fetch_completion
from ..models import GPT3CompletionResponse
from .mocks import MOCK_GPT3_PARAMS, MOCK_PROMPT


@patch("conversation_assistant.gpt3.Completion.create")
def test_fetch_completion__when_all_gpt3_params_passed__then_each_param_mapped_to_api_param(create_completion_spy: MagicMock):
    mock_gpt3_params: GPT3Params = {
        "api_key": "abc123",
        "n": 1,
        "temperature": 0.7,
        "max_tokens": 50,
        "top_p": 1.0,
        "best_of": 1,
        "frequency_penalty": 2.0,
        "presence_penalty": 2.0,
        "stop": ["\n"],
    }
    mock_prompt = """
The following is a conversation between Chad Johnson and Stacey, who is Chad Johnson's new match on a dating app.  
Chad Johnson is a 26 year old Software Developer who lives in Camberwell, Victoria, Australia.
Chad Johnson's pronouns are he/him.
Chad Johnson's favourite hobbies include Coding, Reading books, People watching.  
Chad Johnson can be described as Mysterious, Intriguing, Intelligent.  
The tone of this conversation is Chill, Friendly, Cutesy.

Stacey: It must be my lucky day.
Chad Johnson:"""

    fetch_completion(mock_prompt, mock_gpt3_params)

    # for key in create_completion_spy.call_args_list[0][1].keys():
    #     assert key in mock_gpt3_params.keys()
    call_dict = create_completion_spy.call_args_list[0][1]

    assert call_dict["api_key"] is mock_gpt3_params["api_key"]
    assert call_dict["n"] is mock_gpt3_params["n"]
    assert call_dict["temperature"] is mock_gpt3_params["temperature"]
    assert call_dict["max_tokens"] is mock_gpt3_params["max_tokens"]
    assert call_dict["top_p"] is mock_gpt3_params["top_p"]
    assert call_dict["best_of"] is mock_gpt3_params["best_of"]
    assert call_dict["frequency_penalty"] is mock_gpt3_params["frequency_penalty"]
    assert call_dict["presence_penalty"] is mock_gpt3_params["presence_penalty"]
    assert call_dict["stop"] is mock_gpt3_params["stop"]
