from conversation_assistant.gpt3 import fetch_completetion
from conversation_assistant.models.gpt3_completion_response import GPT3CompletionResponse
from conversation_assistant.test.mock_chatlog import MOCK_CHATLOG


def test_fetch_completetion_returns_3_choices():
    completion_response: GPT3CompletionResponse = fetch_completetion(MOCK_CHATLOG)

    assert len(completion_response["choices"]) == 3
