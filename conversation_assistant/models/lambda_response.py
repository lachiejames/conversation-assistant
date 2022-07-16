from typing_extensions import TypedDict

from .suggestion import Suggestion

GenerateSuggestionsResponse = TypedDict(
    "GenerateSuggestionsResponse",
    {
        "results": list[Suggestion],
    },
)


LambdaResponse = TypedDict(
    "LambdaResponse",
    {
        "statusCode": int,
        "headers": dict[str, str],
        "body": str,
    },
)
