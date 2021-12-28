from conversation_assistant.gpt3 import get_suggestions_for_next_message
from conversation_assistant.test.mock_chatlog import MOCK_CHATLOG


def test_run():
    message_suggestions: list[str] = get_suggestions_for_next_message(MOCK_CHATLOG)

    assert len(message_suggestions) == 3
