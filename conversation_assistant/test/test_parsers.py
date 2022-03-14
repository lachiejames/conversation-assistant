from ..models import Message, Suggestion
from ..parsers import generate_prompt, map_completion_response_to_suggestions
from .mocks import (
    MOCK_COMPLETION_RESPONSE,
    MOCK_MESSAGES,
    MOCK_PROMPT,
    MOCK_SUGGESTIONS,
)


def test_map_completion_response_to_suggestions_returns_expected_suggestions():
    suggestions: list[Suggestion] = map_completion_response_to_suggestions(MOCK_COMPLETION_RESPONSE)

    assert suggestions == MOCK_SUGGESTIONS


def test_map_messages_to_prompt_concatenates_author_with_text():
    prompt: list[Message] = generate_prompt(MOCK_MESSAGES)

    assert prompt == MOCK_PROMPT
