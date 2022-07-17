from typing_extensions import TypedDict

from .suggestion import Suggestion

GenerateSuggestionsResponseBody = TypedDict(
    "GenerateSuggestionsResponseBody",
    {
        "results": list[Suggestion],
    },
)


GenerateSuggestionsResponse = tuple[str, int, dict[str, str]]
