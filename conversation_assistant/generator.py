from .gpt3 import fetch_completion, get_stop_indicator
from .models import GenerateSuggestionsRequest, GPT3CompletionResponse, Suggestion
from .parsers import generate_prompt, map_completion_response_to_suggestions
from .translate import detect_input_lang, translate_text


def fetch_suggestions(request: GenerateSuggestionsRequest) -> list[Suggestion]:
    prompt: str = generate_prompt(request)
    print(f"Constructed prompt:\n'{prompt}'")

    my_name: str = request["settings"]["profile_params"]["name"]
    their_name: str = request["settings"]["conversation_params"]["their_name"]
    stop_indicator: list[str] = get_stop_indicator(my_name, their_name)

    input_lang: str = detect_input_lang(request["previous_messages"])
    print(f"Detected input language: '{input_lang}'")

    translated_prompt: str = translate_text(prompt, input_lang)
    print(f"Translated prompt\n'{translated_prompt}'")

    completion_response: GPT3CompletionResponse = fetch_completion(translated_prompt, request["settings"]["gpt3_params"], stop_indicator)
    print(f"Fetched GPT3 completion response - {completion_response}")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print(f"Generated suggestions - {suggestions}")

    return suggestions
