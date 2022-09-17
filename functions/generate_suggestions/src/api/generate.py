from ..models import (
    GenerateSuggestionsRequest,
    GenerateSuggestionsResponse,
    GPT3CompletionResponse,
    Message,
    Suggestion,
)
from ..prompt import construct_prompt
from ..utils import detect_input_lang
from .gpt3 import fetch_completion, get_stop_indicator
from .parse import map_completion_response_to_suggestions


def stringify_previous_messages(previous_messages: list[Message]) -> str:
    return str([message["text"] for message in previous_messages])


def generate_suggestions(request: GenerateSuggestionsRequest) -> GenerateSuggestionsResponse:
    conversation_sample = stringify_previous_messages(request["previous_messages"])
    input_lang: str = detect_input_lang(conversation_sample)
    print(f"Detected conversation language: '{input_lang}'")

    translated_prompt: str = construct_prompt(request, input_lang)
    print("Constructed prompt")

    stop_indicator: list[str] = get_stop_indicator(request)
    completion_response: GPT3CompletionResponse = fetch_completion(
        prompt=translated_prompt,
        gpt3_params=request["settings"]["gpt3_params"],
        stop_indicator=stop_indicator,
        uid=request["uid"],
    )
    print("Fetched GPT3 completion response")

    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)
    print("Generated suggestions")

    return {
        "suggestions": suggestions,
        "gpt3_usage": completion_response["usage"],
    }
