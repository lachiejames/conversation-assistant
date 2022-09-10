from ..models import GenerateSuggestionsRequest
from ..utils import is_not_empty
from .render import render_template

INTRO_PATH = "extra"


def select_extra_templates(hobbies: str, self_description: str) -> list[str]:
    extra_templates = []

    if is_not_empty(hobbies):
        extra_templates.append(f"{INTRO_PATH}/hobbies.md")
    elif is_not_empty(self_description):
        extra_templates.append(f"{INTRO_PATH}/self_description.md")

    return extra_templates


def render_extra_template(request: GenerateSuggestionsRequest) -> str:
    selected_templates: list[str] = select_extra_templates(
        hobbies=request["settings"]["profile_params"]["hobbies"],
        self_description=request["settings"]["profile_params"]["self_description"],
    )

    prompt_extras = ""
    for template in selected_templates:
        prompt_extras += render_template(request, template)

    return prompt_extras
