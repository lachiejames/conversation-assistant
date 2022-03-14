from ..generator import generate_message_suggestions
from ..models import Suggestion
from ..test.mocks import MOCK_GENERATE_MESSAGE_SUGGESTIONS_REQUEST


def test_generate_message_suggestions_returns_3_choices():
    message_suggestions: list[Suggestion] = generate_message_suggestions(MOCK_GENERATE_MESSAGE_SUGGESTIONS_REQUEST)

    assert len(message_suggestions) == 3
