from typing_extensions import TypedDict

GPT3CompletionChoices = TypedDict(
    "GPT3CompletionChoices",
    {
        "finish_reason": str,
        "index": int,
        "logprobs": None,
        "text": str,
    },
)


GPT3CompletionResponse = TypedDict(
    "GPT3CompletionResponse",
    {
        "choices": list[GPT3CompletionChoices],
        "created": int,
        "id": str,
        "model": str,
        "object": str,
    },
)
