from typing_extensions import TypedDict

from .suggestion import Suggestion

GenerateSuggestionsResponse = TypedDict(
    "GenerateSuggestionsResponse",
    {
        "results": list[Suggestion],
    },
)
