import json

from ...models import GenerateSuggestionsResponse, Suggestion
from .gpt3_responses import MOCK_GPT3_COMPLETION_RESPONSE

MOCK_SUGGESTIONS: list[Suggestion] = [
    {"text": "Hey! I'm Chad, 26 years old and a software developer. What about you?"},
    {"text": "Hey there!"},
    {"text": "From your profile it looks like we have a lot in common so I'd love to chat with you more if you're interested?"},
]

MOCK_SUGGESTIONS_ITALIAN: list[Suggestion] = [
    {"text": "Ehi! Sono Chad, 26 anni e uno sviluppatore di software. E tu?"},
]

MOCK_RESPONSE: GenerateSuggestionsResponse = {
    "suggestions": MOCK_SUGGESTIONS,
    "gpt3_usage": MOCK_GPT3_COMPLETION_RESPONSE["usage"],
}
