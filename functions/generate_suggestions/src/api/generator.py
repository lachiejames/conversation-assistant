from ..models import (
    GenerateSuggestionsRequest,
    GPT3CompletionResponse,
    Message,
    Suggestion,
)
from .gpt3 import fetch_completion, get_stop_indicator
from .parsers import construct_prompt, map_completion_response_to_suggestions
from .translate import detect_input_lang


def stringify_previous_messages(previous_messages: list[Message]) -> str:
    return str([message["text"] for message in previous_messages])


def generate_suggestions(request: GenerateSuggestionsRequest) -> list[Suggestion]:
    conversation_sample = stringify_previous_messages(request["previous_messages"])
    input_lang: str = detect_input_lang(conversation_sample)
    print(f"Detected conversation language: '{input_lang}'")

    translated_prompt: str = construct_prompt(request, input_lang)
    print(f"Constructed prompt:\n'{translated_prompt}'")

    stop_indicator: list[str] = get_stop_indicator(request)
    completion_response: GPT3CompletionResponse = fetch_completion(translated_prompt, request["settings"]["gpt3_params"], stop_indicator)
    print(f"Fetched GPT3 completion response - {completion_response}")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print(f"Generated suggestions - {suggestions}")

    return suggestions
