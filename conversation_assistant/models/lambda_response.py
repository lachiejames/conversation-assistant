from typing_extensions import TypedDict

from .suggestion import Suggestion

GenerateMessageSuggestionsRequest = TypedDict(
    "GenerateMessageSuggestionsRequest",
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
