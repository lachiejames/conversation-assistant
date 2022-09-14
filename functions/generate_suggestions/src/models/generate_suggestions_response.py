from typing_extensions import TypedDict

from .suggestion import Suggestion

GPT3Usage = TypedDict(
    "GenerateSuggestionsResponse",
    {
        "results": list[Suggestion],
        "usage": {
            "completion_tokens": int,
            "prompt_tokens": int,
            "total_tokens": int,
        },
    },
)

GenerateSuggestionsResponse = TypedDict(
    "GenerateSuggestionsResponse",
    {
        "results": list[Suggestion],
        "gpt3_usage": {
            "completion_tokens": int,
            "prompt_tokens": int,
            "total_tokens": int,
        },
    },
)
