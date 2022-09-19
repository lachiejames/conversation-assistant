from ...models import GPT3CompletionResponse

MOCK_GPT3_COMPLETION_RESPONSE: GPT3CompletionResponse = {
    "created": 1640749603,
    "id": "cmpl-4KKDDxKagCnzfBz74m0I5lwpToXjm",
    "model": "davinci-instruct-v3:2021-11-19",
    "object": "text_completion",
    "usage": {
        "completion_tokens": 7,
        "prompt_tokens": 135,
        "total_tokens": 142,
    },
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
}
