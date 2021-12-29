from conversation_assistant.models.suggestion import Suggestion
from conversation_assistant.parsers import parse_message_suggestions
from conversation_assistant.test.mocks import MOCK_COMPLETION_RESPONSE, MOCK_SUGGESTIONS


def test_parse_message_suggestions_returns_expected_suggestions():
    suggestions: list[Suggestion] = parse_message_suggestions(MOCK_COMPLETION_RESPONSE)

    assert suggestions == MOCK_SUGGESTIONS
