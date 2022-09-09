from ..models import (
    GenerateSuggestionsRequest,
    GPT3CompletionResponse,
    Suggestion,
)
from .translate import DEFAULT_LANG, UNDEFINED_LANG, translate_text
from jinja2 import Environment, PackageLoader, select_autoescape


def is_empty(field: str) -> bool:
    return len(field) == 0


def select_base_template(my_name: str, their_name: str) -> str:
    if is_empty(my_name) or is_empty(their_name):
        return "names_missing.md"
    else:
        return "nothing_missing.md"


def select_extra_templates(my_name: str, their_name: str) -> list[str]:
    if is_empty(my_name) or is_empty(their_name):
        return "names_missing.md"
    else:
        return "nothing_missing.md"


def select_templates(request: GenerateSuggestionsRequest) -> list[str]:
    templates = []
    templates.append(
        select_base_template(
            my_name=request["settings"]["profile_params"]["name"],
            their_name=request["settings"]["conversation_params"]["their_name"],
        ),
    ),
    templates.extend(
        select_extra_templates(
            my_name=request["settings"]["profile_params"]["name"],
            their_name=request["settings"]["conversation_params"]["their_name"],
        ),
    )

    return templates


def generate_prompt(request: GenerateSuggestionsRequest, input_lang: str) -> str:
    prompt = ""
    env = Environment(
        loader=PackageLoader(package_name="src"),
        autoescape=select_autoescape(),
        keep_trailing_newline=True,
    )

    for template in select_templates(request):
        prompt += env.get_template(template).render(
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
        )

    if input_lang != DEFAULT_LANG and input_lang != UNDEFINED_LANG:
        prompt = translate_text(prompt, input_lang)
    
    prompt += env.get_template("messages.md").render(previous_messages=request["previous_messages"])

    return prompt


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].strip()
        suggestions.append({"text": suggestion})

    return suggestions
