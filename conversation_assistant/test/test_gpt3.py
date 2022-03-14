from ..gpt3 import fetch_completion
from ..models import GPT3CompletionResponse
from .mocks import MOCK_GPT3_PARAMS, MOCK_PROMPT


def test_fetch_completion_returns_3_choices():
    completion_response: GPT3CompletionResponse = fetch_completion(MOCK_PROMPT, MOCK_GPT3_PARAMS)

    assert len(completion_response["choices"]) == 3
