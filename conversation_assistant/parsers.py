from conversation_assistant.models.gpt3_completion_response import GPT3CompletionResponse
from conversation_assistant.models.suggestion import Suggestion


def parse_message_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestions.append({"text": choice["text"].lstrip()})

    return suggestions
