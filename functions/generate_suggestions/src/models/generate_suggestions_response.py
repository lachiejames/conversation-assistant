from typing_extensions import TypedDict

from .gpt3_completion_response import GPT3Usage
from .suggestion import Suggestion

GenerateSuggestionsResponse = TypedDict(
    "GenerateSuggestionsResponse",
    {
        "suggestions": list[Suggestion],
        "gpt3_usage": GPT3Usage,
    },
)
