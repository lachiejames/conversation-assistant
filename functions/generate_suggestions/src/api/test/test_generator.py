from unittest.mock import MagicMock, patch

from ...models import GenerateSuggestionsResponse
from ...test.mocks import MOCK_GPT3_COMPLETION_RESPONSE, EMPTY_REQUEST, MOCK_SUGGESTIONS
from ..generate import generate_suggestions


@patch("src.generate.fetch_completion", MagicMock(return_value=MOCK_GPT3_COMPLETION_RESPONSE))
@patch("src.generate.detect_input_lang", MagicMock(return_value="en"))
def test_generate_suggestions__when_request_is_valid__then_returns_parsed_suggestions_from_gpt3() -> None:
    mock_response: GenerateSuggestionsResponse = generate_suggestions(EMPTY_REQUEST)

    assert mock_response["suggestions"] == MOCK_SUGGESTIONS
