from unittest.mock import MagicMock, patch

from ..generator import fetch_suggestions
from ..models import Suggestion
from .mocks import (
    MOCK_GPT3_COMPLETION_RESPONSE,
    MOCK_PROMPT,
    MOCK_REQUEST,
    MOCK_SUGGESTIONS,
)


@patch("conversation_assistant.generator.fetch_completion", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
@patch("conversation_assistant.generator.detect_input_lang", MagicMock(return_value="en"))
@patch("conversation_assistant.generator.translate_text", MagicMock(return_value={"translatedText": MOCK_PROMPT}))
def test_fetch_suggestions__when_request_is_valid__then_returns_parsed_suggestions_from_gpt3() -> None:
    message_suggestions: list[Suggestion] = fetch_suggestions(MOCK_REQUEST)

    assert message_suggestions == MOCK_SUGGESTIONS
