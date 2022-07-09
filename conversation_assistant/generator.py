from .gpt3 import fetch_completion, get_stopper
from .models import (
    GenerateMessageSuggestionsRequest,
    GPT3CompletionResponse,
    Suggestion,
)
from .parsers import generate_prompt, map_completion_response_to_suggestions


def generate_message_suggestions(request: GenerateMessageSuggestionsRequest):
    prompt: str = generate_prompt(request)
    print(f"Constructed a prompt - {prompt}")

    my_name: str = request["settings"]["profile_params"]["name"]
    their_name: str = request["settings"]["conversation_params"]["their_name"]
    stopper: list[str] = get_stopper(my_name, their_name)

    completion_response: GPT3CompletionResponse = fetch_completion(prompt, request["settings"]["gpt3_params"], stopper)
    print(f"Fetched GPT3 completion response - {completion_response}")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print(f"Generated suggestions - {suggestions}")

    return suggestions
