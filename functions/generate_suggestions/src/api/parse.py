from ..models import GPT3CompletionResponse, Suggestion


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].strip()
        suggestions.append({"text": suggestion})

    return suggestions
