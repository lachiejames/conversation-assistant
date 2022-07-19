from .gpt3 import fetch_completion, get_stop_indicator
from .models import GenerateSuggestionsRequest, GPT3CompletionResponse, Suggestion
from .parsers import generate_prompt, map_completion_response_to_suggestions
from .translate import detect_input_lang


def fetch_suggestions(request: GenerateSuggestionsRequest) -> list[Suggestion]:
    conversation_sample = str([message["text"] for message in request["previous_messages"]])
    input_lang: str = detect_input_lang(conversation_sample)
    print(f"Detected input language: '{input_lang}'")

    translated_prompt: str = generate_prompt(request, input_lang)
    print(f"Constructed prompt:\n'{translated_prompt}'")


    stop_indicator: list[str] = get_stop_indicator(request)

    completion_response: GPT3CompletionResponse = fetch_completion(translated_prompt, request["settings"]["gpt3_params"], stop_indicator)
    print(f"Fetched GPT3 completion response - {completion_response}")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print(f"Generated suggestions - {suggestions}")

    return suggestions
