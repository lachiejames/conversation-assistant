from ..models import ConversationParams, Message, ProfileParams, Suggestion
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
    mock_profile_params: ProfileParams = MOCK_REQUEST["settings"]["profile_params"]
    mock_conversation_params: ConversationParams = MOCK_REQUEST["settings"]["conversation_params"]
    mock_previous_messages: list[Message] = MOCK_REQUEST["previous_messages"]

    prompt: list[Message] = generate_prompt(mock_profile_params, mock_conversation_params, mock_previous_messages)

    assert prompt == MOCK_PROMPT


def test_generate_prompt__when_all_params_are_empty___then_returns_silly_looking_prompt_without_raising_error():
    mock_profile_params: ProfileParams = {
        "name": "",
        "age": -1,
        "pronouns": "",
        "location": "",
        "occupation": "",
        "hobbies": [],
        "traits": [],
    }
    mock_conversation_params: ConversationParams = {
        "their_name": "",
        "their_relationship_to_me": "",
        "tone_of_chat": [],
    }

    mock_previous_messages: list[Message] = []

    expected_silly_prompt = """
The following is a conversation between  and , who is 's .  
 is a -1 year old  who lives in .
's pronouns are .
's favourite hobbies include .  
 can be described as .  
The tone of this conversation is .

:"""

    prompt: list[Message] = generate_prompt(mock_profile_params, mock_conversation_params, mock_previous_messages)

    assert prompt == expected_silly_prompt
