from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix, is_not_empty
from .render import render_template


def select_extra_templates(
    path_prefix: str,
    age: str,
    pronouns: str,
    location: str,
    occupation: str,
    hobbies: str,
    self_description: str,
) -> list[str]:
    extra_templates = []

    if is_not_empty(age):
        extra_templates.append(f"{path_prefix}/age.md")
    if is_not_empty(pronouns):
        extra_templates.append(f"{path_prefix}/pronouns.md")
    if is_not_empty(location):
        extra_templates.append(f"{path_prefix}/location.md")
    if is_not_empty(occupation):
        extra_templates.append(f"{path_prefix}/occupation.md")
    if is_not_empty(hobbies):
        extra_templates.append(f"{path_prefix}/hobbies.md")
    if is_not_empty(self_description):
        extra_templates.append(f"{path_prefix}/self_description.md")

    return extra_templates


def render_extra_template(request: GenerateSuggestionsRequest) -> str:
    selected_templates: list[str] = select_extra_templates(
        path_prefix=f"{choose_path_prefix(request)}/extra",
        age=request["settings"]["profile_params"]["age"],
        pronouns=request["settings"]["profile_params"]["pronouns"],
        location=request["settings"]["profile_params"]["location"],
        occupation=request["settings"]["profile_params"]["occupation"],
        hobbies=request["settings"]["profile_params"]["hobbies"],
        self_description=request["settings"]["profile_params"]["self_description"],
    )

    prompt_extras = ""
    for template in selected_templates:
        prompt_extras += render_template(request, template)

    return prompt_extras
