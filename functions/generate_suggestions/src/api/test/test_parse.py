from ...models import Suggestion
from ...test.mocks import MOCK_GPT3_COMPLETION_RESPONSE_DICT, MOCK_SUGGESTIONS
from ..parse import map_completion_response_to_suggestions


def test_map_completion_response_to_suggestions_returns_expected_suggestions() -> None:
    suggestions: list[Suggestion] = map_completion_response_to_suggestions(MOCK_GPT3_COMPLETION_RESPONSE_DICT)

    assert suggestions == MOCK_SUGGESTIONS
