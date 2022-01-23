from typing_extensions import TypedDict

from conversation_assistant.models.suggestion import Suggestion

MessageSuggestions = TypedDict(
    "MessageSuggestions",
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
