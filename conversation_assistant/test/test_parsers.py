from ..models import ConversationParams, Message, ProfileParams, Suggestion
from ..parsers import generate_prompt, map_completion_response_to_suggestions
from .mocks import MOCK_GPT3_COMPLETION_RESPONSE, MOCK_SUGGESTIONS


def test_map_completion_response_to_suggestions_returns_expected_suggestions():
    suggestions: list[Suggestion] = map_completion_response_to_suggestions(MOCK_GPT3_COMPLETION_RESPONSE)

    assert suggestions == MOCK_SUGGESTIONS


def test_generate_prompt__when_all_params_defined___then_returns_prompt_containing_all_params():
    mock_profile_params: ProfileParams = {
        "name": "Chad Johnson",
        "age": 26,
        "pronouns": "he/him",
        "location": "Camberwell, Victoria, Australia",
        "occupation": "Software Developer",
        "hobbies": ["Coding", "Reading books", "People watching"],
        "traits": ["Mysterious", "Intriguing", "Intelligent"],
    }
    mock_conversation_params: ConversationParams = {
        "their_name": "Stacey",
        "their_relationship_to_me": "new match on a dating app",
        "tone_of_chat": ["Chill", "Friendly", "Cutesy"],
        "previous_messages": [
            {
                "text": "It must be my lucky day.",
                "author": "Stacey",
            },
        ],
    }

    expected_prompt = """
The following is a conversation between Chad Johnson and Stacey, who is Chad Johnson's new match on a dating app.  
Chad Johnson is a 26 year old Software Developer who lives in Camberwell, Victoria, Australia.
Chad Johnson's pronouns are he/him.
Chad Johnson's favourite hobbies include Coding, Reading books, People watching.  
Chad Johnson can be described as Mysterious, Intriguing, Intelligent.  
The tone of this conversation is Chill, Friendly, Cutesy.

Stacey: It must be my lucky day.
Chad Johnson:"""

    prompt: list[Message] = generate_prompt(mock_profile_params, mock_conversation_params)

    assert prompt == expected_prompt


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
        "previous_messages": [],
    }

    expected_silly_prompt = """
The following is a conversation between  and , who is 's .  
 is a -1 year old  who lives in .
's pronouns are .
's favourite hobbies include .  
 can be described as .  
The tone of this conversation is .

:"""

    prompt: list[Message] = generate_prompt(mock_profile_params, mock_conversation_params)

    assert prompt == expected_silly_prompt
