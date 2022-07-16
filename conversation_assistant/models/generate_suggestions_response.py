from typing_extensions import TypedDict

from .suggestion import Suggestion

GenerateSuggestionsResponseBody = TypedDict(
    "GenerateSuggestionsResponseBody",
    {
        "results": list[Suggestion],
    },
)


GenerateSuggestionsResponse = TypedDict(
    "GenerateSuggestionsResponse",
    {
        "statusCode": int,
        "headers": dict[str, str],
        "body": str,
    },
)
