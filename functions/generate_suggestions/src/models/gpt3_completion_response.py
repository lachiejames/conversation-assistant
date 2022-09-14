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

GPT3Usage = TypedDict(
    "GPT3Usage",
    {
        "completion_tokens": int,
        "prompt_tokens": int,
        "total_tokens": int,
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
        "usage": GPT3Usage,
    },
)
