from ..models import (
    ConversationParams,
    GenerateMessageSuggestionsRequest,
    Message,
    ProfileParams,
    Suggestion,
)
from ..parsers import generate_prompt, map_completion_response_to_suggestions
from .mocks import (
    MOCK_GPT3_COMPLETION_RESPONSE,
    MOCK_PROMPT,
    MOCK_REQUEST,
    MOCK_SUGGESTIONS,
)


def test_map_completion_response_to_suggestions_returns_expected_suggestions():
    suggestions: list[Suggestion] = map_completion_response_to_suggestions(MOCK_GPT3_COMPLETION_RESPONSE)

    assert suggestions == MOCK_SUGGESTIONS


def test_generate_prompt__when_all_params_defined___then_returns_prompt_containing_all_params():
    prompt: list[Message] = generate_prompt(MOCK_REQUEST)

    assert prompt == MOCK_PROMPT


def test_generate_prompt__when_all_params_are_empty___then_returns_silly_looking_prompt_without_raising_error():
    mock_profile_params: ProfileParams = {
        "name": "",
        "age": "",
        "pronouns": "",
        "location": "",
        "occupation": "",
        "hobbies": "",
        "self_description": "",
    }
    mock_conversation_params: ConversationParams = {
        "their_name": "",
        "their_relationship_to_me": "",
        "tone_of_chat": "",
    }

    mock_previous_messages: list[Message] = []

    request: GenerateMessageSuggestionsRequest = {
        "previous_messages": mock_previous_messages,
        "settings": {
            "profile_params": mock_profile_params,
            "conversation_params": mock_conversation_params,
            "gpt3_params": MOCK_REQUEST["settings"]["gpt3_params"],
        },
    }

    expected_silly_prompt = """
The following is a conversation between  and , who is 's .
 is a  year old  who lives in .
's pronouns are .
's favourite hobbies include .
 can be described as .
The tone of this conversation is .

:"""

    prompt: list[Message] = generate_prompt(request)

    assert prompt == expected_silly_prompt
