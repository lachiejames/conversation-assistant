from ..models import GenerateSuggestionsRequest

from jinja2 import Environment, PackageLoader, select_autoescape

template_env = Environment(
    loader=PackageLoader(package_path="prompt_templates"),
    autoescape=select_autoescape(),
    keep_trailing_newline=True,
)

def render_template(request: GenerateSuggestionsRequest, template: str) -> str:
    return template_env.get_template(template).render(
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
