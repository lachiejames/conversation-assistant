from unittest.mock import MagicMock, patch

from ...models import Suggestion
from ...test.mocks import (
    MOCK_GPT3_COMPLETION_RESPONSE,
    MOCK_PROMPT_PREFIX,
    MOCK_REQUEST,
    MOCK_SUGGESTIONS,
)
from ..generator import generate_suggestions


@patch("src.generator.fetch_completion", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
@patch("src.generator.detect_input_lang", MagicMock(return_value="en"))
@patch("src.parsers.translate_text", MagicMock(return_value=MOCK_PROMPT_PREFIX))
def test_generate_suggestions__when_request_is_valid__then_returns_parsed_suggestions_from_gpt3() -> None:
    message_suggestions: list[Suggestion] = generate_suggestions(MOCK_REQUEST)

    assert message_suggestions == MOCK_SUGGESTIONS
