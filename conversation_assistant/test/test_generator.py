from conversation_assistant.generator import generate_message_suggestions
from conversation_assistant.models import Suggestion
from conversation_assistant.test.mocks import MOCK_LAMBDA_EVENT


def test_generate_message_suggestions_returns_3_choices():
    message_suggestions: list[Suggestion] = generate_message_suggestions(MOCK_LAMBDA_EVENT)

    assert len(message_suggestions) == 3
