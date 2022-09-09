from ..models import (
    GenerateSuggestionsRequest,
    GPT3CompletionResponse,
    Suggestion,
)
from .translate import DEFAULT_LANG, UNDEFINED_LANG, translate_text
from jinja2 import Environment, PackageLoader, select_autoescape


def is_empty(field: str) -> bool:
    return len(field) == 0

def select_template(request: GenerateSuggestionsRequest) -> str:
    conversation = request["settings"]["conversation_params"]
    profile = request["settings"]["profile_params"]
    is_their_name_empty = is_empty(conversation["their_name"])
    is_my_name_empty = is_empty(profile["name"])
 
    if (is_their_name_empty or is_my_name_empty) and is_empty(conversation["their_relationship_to_me"]):
        return "names_missing.md"
    else:
        return "nothing_missing.md"


def generate_prompt(request: GenerateSuggestionsRequest, input_lang: str) -> str:
    env = Environment(
        loader=PackageLoader(package_name="src"),
        autoescape=select_autoescape(),
        keep_trailing_newline=True,
    )
    template_file_name = select_template(request)
    template = env.get_template(template_file_name)

    return template.render(
        my_name=request["settings"]["profile_params"]["name"],
        my_age=request["settings"]["profile_params"]["age"],
        my_pronouns=request["settings"]["profile_params"]["pronouns"],
        my_location=request["settings"]["profile_params"]["location"],
        my_occupation=request["settings"]["profile_params"]["occupation"],
        my_hobbies=request["settings"]["profile_params"]["hobbies"],
        my_self_description=request["settings"]["profile_params"]["self_description"],
        their_name=request["settings"]["conversation_params"]["their_name"],
        their_relationship_to_me=request["settings"]["conversation_params"]["their_relationship_to_me"],
        tone_of_chat=request["settings"]["conversation_params"]["tone_of_chat"],
        previous_messages=request["previous_messages"],
    )


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].strip()
        suggestions.append({"text": suggestion})

    return suggestions
