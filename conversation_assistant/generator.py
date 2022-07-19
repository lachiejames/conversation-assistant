from .gpt3 import fetch_completion, get_stop_indicator
from .models import GenerateSuggestionsRequest, GPT3CompletionResponse, Suggestion
from .parsers import generate_prompt, map_completion_response_to_suggestions


def fetch_suggestions(request: GenerateSuggestionsRequest) -> list[Suggestion]:
    prompt: str = generate_prompt(request)
    print(f"Constructed a prompt - {prompt}")

    my_name: str = request["settings"]["profile_params"]["name"]
    their_name: str = request["settings"]["conversation_params"]["their_name"]
    stop_indicator: list[str] = get_stop_indicator(my_name, their_name)

    completion_response: GPT3CompletionResponse = fetch_completion(prompt, request["settings"]["gpt3_params"], stop_indicator)
    print(f"Fetched GPT3 completion response - {completion_response}")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print(f"Generated suggestions - {suggestions}")

    return suggestions
