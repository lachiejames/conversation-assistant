from ..models import (
    GenerateSuggestionsRequest,
    GPT3CompletionResponse,
    Suggestion,
)
from .translate import DEFAULT_LANG, UNDEFINED_LANG, translate_text
from jinja2 import Environment, PackageLoader, select_autoescape


def is_empty(field: str) -> bool:
    return len(field) == 0

def get_template_env() -> Environment:
    return Environment(
        loader=PackageLoader(package_name="src", package_path="templates"),
        autoescape=select_autoescape(),
        keep_trailing_newline=True,
    )


def select_intro_template(my_name: str, their_name: str) -> str:
    if is_empty(my_name) or is_empty(their_name):
        return "intro/no_names.md"
    else:
        return "intro/complete.md"


def select_extra_templates(hobbies: str, self_description: str) -> list[str]:
    extra_templates = []

    if not is_empty(hobbies):
        extra_templates.append("extras/hobbies.md")
    elif not is_empty(self_description):
        extra_templates.append("extras/self_description.md")

    return extra_templates


def choose_prompt_templates(request: GenerateSuggestionsRequest) -> list[str]:
    templates = []
    templates.append(
        select_intro_template(
            my_name=request["settings"]["profile_params"]["name"],
            their_name=request["settings"]["conversation_params"]["their_name"],
        ),
    ),
    templates.extend(
        select_extra_templates(
            hobbies=request["settings"]["profile_params"]["hobbies"],
            self_description=request["settings"]["profile_params"]["self_description"],
        ),
    )

    return templates


def construct_prompt(request: GenerateSuggestionsRequest, input_lang: str) -> str:
    prompt = ""
    template_env = get_template_env()
    selected_templates = choose_prompt_templates(request)

    for template in choose_prompt_templates(request):
        prompt += template_env.get_template(template).render(
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

    prompt += template_env.get_template("messages.md").render(
        previous_messages=request["previous_messages"],
    )

    prompt += template_env.get_template("suggestion.md").render(
        my_name=request["settings"]["profile_params"]["name"],
    )

    return prompt


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].strip()
        suggestions.append({"text": suggestion})

    return suggestions
