from .gpt3 import fetch_completion
from .models import (
    GenerateMessageSuggestionsRequest,
    GPT3CompletionResponse,
    Suggestion,
)
from .parsers import generate_prompt, map_completion_response_to_suggestions


def generate_message_suggestions(request: GenerateMessageSuggestionsRequest):
    prompt: str = generate_prompt(request)
    print(f"Constructed a prompt - {prompt}")

    completion_response: GPT3CompletionResponse = fetch_completion(prompt, request["gpt3_params"], request["auth_params"]["api_key"])
    print(f"Fetched GPT3 completion response - {completion_response}")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print(f"Generated suggestions - {suggestions}")

    return suggestions
