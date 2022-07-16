from unittest.mock import MagicMock, patch

from ..generator import generate_message_suggestions
from ..models import Suggestion
from .mocks import MOCK_GPT3_COMPLETION_RESPONSE, MOCK_REQUEST_BODY, MOCK_SUGGESTIONS


@patch("conversation_assistant.generator.fetch_completion", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
def test_generate_message_suggestions__when_request_is_valid__then_returns_parsed_suggestions_from_gpt3():
    message_suggestions: list[Suggestion] = generate_message_suggestions(MOCK_REQUEST_BODY)

    assert message_suggestions == MOCK_SUGGESTIONS
