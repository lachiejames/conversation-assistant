from typing import cast

from ...models import GenerateSuggestionsRequest

MOCK_REQUEST: GenerateSuggestionsRequest = {
    "uid": "abc123",
    "previous_messages": [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ],
    "settings": {
        "profile_params": {
            "name": "Chad Johnson",
            "age": "27",
            "pronouns": "he/him",
            "location": "Camberwell, Victoria, Australia",
            "occupation": "Software Engineer",
            "hobbies": "coding, hanging out with my dog",
            "self_description": "a cool guy who always knows the right thing to say",
        },
        "conversation_params": {
            "their_name": "Stacey",
            "their_relationship_to_me": "Friend",
            "tone_of_chat": "Casual",
            "message_to_rephrase": "Well hot diggity dog!",
        },
        "gpt3_params": {
            "engine": "text-davinci-002",
            "n": 1,
            "temperature": 1.0,
            "max_tokens": 50,
            "best_of": 1,
            "frequency_penalty": 1.0,
            "presence_penalty": 1.0,
        },
    },
}

MOCK_REQUEST_NO_NAMES: GenerateSuggestionsRequest = cast(
    GenerateSuggestionsRequest,
    MOCK_REQUEST
    | {
        "settings": MOCK_REQUEST["settings"]
        | {
            "profile_params": MOCK_REQUEST["settings"]["profile_params"]
            | {
                "name": "",
            },
            "conversation_params": MOCK_REQUEST["settings"]["conversation_params"]
            | {
                "their_name": "",
            },
        }
    },
)


MOCK_REQUEST_NO_MESSAGES: GenerateSuggestionsRequest = cast(GenerateSuggestionsRequest, MOCK_REQUEST | {"previous_messages": []})

MOCK_REQUEST_NO_NAMES_NO_MESSAGES: GenerateSuggestionsRequest = cast(
    GenerateSuggestionsRequest,
    MOCK_REQUEST
    | {
        "settings": MOCK_REQUEST["settings"]
        | {
            "profile_params": MOCK_REQUEST["settings"]["profile_params"]
            | {
                "name": "",
            },
            "conversation_params": MOCK_REQUEST["settings"]["conversation_params"]
            | {
                "their_name": "",
            },
        },
        "previous_messages": [],
    },
)

MOCK_REQUEST_NO_NAMES_NO_RELATIONSHIP: GenerateSuggestionsRequest = cast(
    GenerateSuggestionsRequest,
    MOCK_REQUEST
    | {
        "settings": MOCK_REQUEST["settings"]
        | {
            "profile_params": MOCK_REQUEST["settings"]["profile_params"]
            | {
                "name": "",
            },
            "conversation_params": MOCK_REQUEST["settings"]["conversation_params"]
            | {
                "their_name": "",
                "their_relationship_to_me": "",
            },
        }
    },
)


MOCK_REQUEST_NOTHING: GenerateSuggestionsRequest = cast(
    GenerateSuggestionsRequest,
    (
        MOCK_REQUEST_NO_NAMES
        | MOCK_REQUEST_NO_MESSAGES
        | {
            "settings": {
                "profile_params": {
                    "name": "",
                    "age": "",
                    "pronouns": "",
                    "location": "",
                    "occupation": "",
                    "hobbies": "",
                    "self_description": "",
                },
                "conversation_params": {
                    "their_name": "",
                    "their_relationship_to_me": "",
                    "tone_of_chat": "",
                    "message_to_rephrase": "",
                },
            },
        }
    ),
)
