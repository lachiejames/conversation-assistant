import os

from openai import Completion

from ..models import GenerateSuggestionsRequest, GPT3CompletionResponse, GPT3Params
from ..utils import is_not_empty, validate_completion_response


def get_stop_indicator(request: GenerateSuggestionsRequest) -> list[str]:
    """Prevents GPT3 from returning a full conversation instead of just 1 message"""

    my_name: str = request["settings"]["profile_params"]["name"]
    their_name: str = request["settings"]["conversation_params"]["their_name"]
    their_relationship_to_me: str = request["settings"]["conversation_params"]["their_relationship_to_me"]

    are_names_given = is_not_empty(my_name) and is_not_empty(their_name)
    is_relationship_given = is_not_empty(their_relationship_to_me)

    if are_names_given:
        return [f"{my_name}:", f"{their_name}:"]
    if is_relationship_given:
        return ["Me:", f"{their_relationship_to_me}:"]
    return ["Me:", "Them:"]


def fetch_completion(prompt: str, gpt3_params: GPT3Params, stop_indicator: list[str], uid: str) -> GPT3CompletionResponse:
    """Depends on OPENAI_API_KEY environment variable"""

    response: GPT3CompletionResponse = Completion.create(
        engine=gpt3_params["engine"],
        prompt=prompt,
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=gpt3_params["temperature"],
        n=gpt3_params["n"],
        max_tokens=gpt3_params["max_tokens"],
        best_of=gpt3_params["best_of"],
        frequency_penalty=gpt3_params["frequency_penalty"],
        presence_penalty=gpt3_params["presence_penalty"],
        stop=stop_indicator,
    )

    validate_completion_response(response)

    return response
