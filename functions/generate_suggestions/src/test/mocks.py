from typing import cast

from ..models import GenerateSuggestionsRequest, GPT3CompletionResponse, Suggestion

MOCK_PROMPT_PREFIX = """
The following is a conversation between Chad Johnson and Stacey, who is Chad Johnson's new match on a dating app.
Chad Johnson is a 26 year old Software Developer who lives in Camberwell, Victoria, Australia.
Chad Johnson's pronouns are he/him.
Chad Johnson's favourite hobbies include coding, reading books, and people watching.
Chad Johnson can be described as mysterious, yet intriguing.
The tone of this conversation is chill."""

MOCK_PROMPT = f"""{MOCK_PROMPT_PREFIX}

Stacey: hey there
Chad Johnson:"""

MOCK_PROMPT_ITALIAN = """
Quella che segue è una conversazione tra Chad Johnson e Stacey, che è la nuova partita di Chad Johnson su un'app di appuntamenti.
Chad Johnson è uno sviluppatore di software di 26 anni che vive a Camberwell, Victoria, Australia.
I pronomi di Chad Johnson sono lui/lui.
Gli hobby preferiti di Chad Johnson includono la programmazione, la lettura di libri e l'osservazione delle persone.
Chad Johnson può essere descritto come misterioso, ma intrigante.
Il tono di questa conversazione è freddo."""

MOCK_SUGGESTIONS: list[Suggestion] = [
    {"text": "Hey! I'm Chad, 26 years old and a software developer. What about you?"},
    {"text": "Hey there!"},
    {"text": "From your profile it looks like we have a lot in common so I'd love to chat with you more if you're interested?"},
]

MOCK_SUGGESTIONS_ITALIAN: list[Suggestion] = [
    {"text": "Ehi! Sono Chad, 26 anni e uno sviluppatore di software. E tu?"},
]

MOCK_GPT3_COMPLETION_RESPONSE: GPT3CompletionResponse = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": None,
            "text": "Hey! I'm Chad, 26 years old and a software developer. What about you?",
        },
        {
            "finish_reason": "stop",
            "index": 1,
            "logprobs": None,
            "text": "Hey there!",
        },
        {
            "finish_reason": "stop",
            "index": 2,
            "logprobs": None,
            "text": "From your profile it looks like we have a lot in common so I'd love to chat with you more if you're interested?",
        },
    ],
    "created": 1640749603,
    "id": "cmpl-4KKDDxKagCnzfBz74m0I5lwpToXjm",
    "model": "davinci-instruct-v3:2021-11-19",
    "object": "text_completion",
}


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
        },
        "gpt3_params": {
            "engine": "text-curie-001",
            "n": 1,
            "temperature": 1.0,
            "max_tokens": 50,
            "best_of": 1,
            "frequency_penalty": 1.0,
            "presence_penalty": 1.0,
            "user": "abc123",
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
                },
            },
        }
    ),
)
