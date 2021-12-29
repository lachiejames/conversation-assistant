from conversation_assistant.models.message import Message
from conversation_assistant.models.suggestion import Suggestion
from conversation_assistant.parsers import map_messages_to_prompt, parse_message_suggestions
from conversation_assistant.test.mocks import MOCK_COMPLETION_RESPONSE, MOCK_MESSAGES, MOCK_PROMPT, MOCK_SUGGESTIONS


def test_parse_message_suggestions_returns_expected_suggestions():
    suggestions: list[Suggestion] = parse_message_suggestions(MOCK_COMPLETION_RESPONSE)

    assert suggestions == MOCK_SUGGESTIONS


def test_map_messages_to_prompt_concatenates_author_with_text():
    prompt: list[Message] = map_messages_to_prompt(MOCK_MESSAGES)

    assert prompt == MOCK_PROMPT
