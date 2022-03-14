import json

from ..models import (
    GenerateMessageSuggestionsRequest,
    GPT3CompletionResponse,
    LambdaEvent,
    Suggestion,
)

MOCK_PROMPT = """
The following is a conversation between Chad Johnson and Stacey, who is Chad Johnson's new match on a dating app.  
Chad Johnson is a 26 year old Software Developer who lives in Camberwell, Victoria, Australia.
Chad Johnson's pronouns are he/him.
Chad Johnson's favourite hobbies include Coding, Reading books, People watching.  
Chad Johnson can be described as Mysterious, Intriguing, Intelligent.  
The tone of this conversation is Chill, Friendly, Cutesy.

Stacey: It must be my lucky day.
Chad Johnson:"""

MOCK_SUGGESTIONS: list[Suggestion] = [
    {"text": "Not much, just been hanging out with friends and family."},
    {"text": "Just been keeping busy mate, you?"},
    {"text": "I've been pretty busy mate, just been doing some work and hanging out with friends."},
]

MOCK_GPT3_COMPLETION_RESPONSE: GPT3CompletionResponse = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "logprobs": None,
            "text": "\nNot much, just been hanging out with friends and family.",
        },
        {
            "finish_reason": "stop",
            "index": 1,
            "logprobs": None,
            "text": "\nJust been keeping busy mate, you?",
        },
        {
            "finish_reason": "stop",
            "index": 2,
            "logprobs": None,
            "text": "I've been pretty busy mate, just been doing some work and hanging out with friends.",
        },
    ],
    "created": 1640749603,
    "id": "cmpl-4KKDDxKagCnzfBz74m0I5lwpToXjm",
    "model": "davinci-instruct-v3:2021-11-19",
    "object": "text_completion",
}


MOCK_REQUEST: GenerateMessageSuggestionsRequest = {
    "profile_params": {
        "name": "Chad Johnson",
        "age": 26,
        "pronouns": "he/him",
        "location": "Camberwell, Victoria, Australia",
        "occupation": "Software Developer",
        "hobbies": ["Coding", "Reading books", "People watching"],
        "traits": ["Mysterious", "Intriguing", "Intelligent"],
    },
    "conversation_params": {
        "their_name": "Stacey",
        "their_relationship_to_me": "new match on a dating app",
        "tone_of_chat": ["Chill", "Friendly", "Cutesy"],
        "previous_messages": [
            {
                "text": "It must be my lucky day.",
                "author": "Stacey",
            },
        ],
    },
    "gpt3_params": {
        "api_key": "abc123",
        "n": 1,
        "temperature": 0.7,
        "max_tokens": 50,
        "top_p": 1.0,
        "best_of": 1,
        "frequency_penalty": 2.0,
        "presence_penalty": 2.0,
        "stop": ["\n"],
    },
}

MOCK_LAMBDA_EVENT: LambdaEvent = {"body": json.dumps(MOCK_REQUEST)}
