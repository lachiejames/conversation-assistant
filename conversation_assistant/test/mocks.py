import json

from ..models import (
    GenerateMessageSuggestionsRequest,
    GPT3CompletionResponse,
    GPT3Params,
    LambdaEvent,
    Message,
    Suggestion,
)

MOCK_MESSAGES: list[Message] = [
    {"text": "Hey, how are you today?", "author": "Lachie James"},
    {"text": "Not too bad mate, how are you?", "author": "Me"},
    {"text": "Yeah good mate.  What have you been up to lately?", "author": "Lachie James"},
]

MOCK_PROMPT = """The following is a conversation between ['Lachie James', 'Me'].
The assistant will give Me suggestions for things to say in this conversation.

Lachie James: Hey, how are you today?
Me: Not too bad mate, how are you?
Lachie James: Yeah good mate.  What have you been up to lately?
Me: """


MOCK_COMPLETION_RESPONSE: GPT3CompletionResponse = {
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


MOCK_SUGGESTIONS: list[Suggestion] = [
    {"text": "Not much, just been hanging out with friends and family."},
    {"text": "Just been keeping busy mate, you?"},
    {"text": "I've been pretty busy mate, just been doing some work and hanging out with friends."},
]

MOCK_GPT3_PARAMS: GPT3Params = {
    "randomness": 0.7,
    "num_results": 3,
    "max_length": 50,
}

MOCK_GENERATE_MESSAGE_SUGGESTIONS_REQUEST: GenerateMessageSuggestionsRequest = {
    "previous_messages": MOCK_MESSAGES,
    "gpt3_params": MOCK_GPT3_PARAMS,
}


MOCK_LAMBDA_EVENT: LambdaEvent = {"body": json.dumps(MOCK_GENERATE_MESSAGE_SUGGESTIONS_REQUEST)}
