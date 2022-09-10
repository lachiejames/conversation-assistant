from ..models import GenerateSuggestionsRequest
from ..api import DEFAULT_LANG, UNDEFINED_LANG, translate_text
from .extra import select_extra_templates
from .intro import select_intro_template
from .message import select_message_template
from .suggestion import select_suggestion_template



def choose_prompt_templates(request: GenerateSuggestionsRequest) -> list[str]:
    templates = []
    templates.append(
        select_intro_template(
            my_name=request["settings"]["profile_params"]["name"],
            their_name=request["settings"]["conversation_params"]["their_name"],
        ),
    )
    templates.extend(
        select_extra_templates(
            hobbies=request["settings"]["profile_params"]["hobbies"],
            self_description=request["settings"]["profile_params"]["self_description"],
        ),
    )

    return templates


def construct_prompt(request: GenerateSuggestionsRequest, input_lang: str) -> str:
    prompt = select_intro_template()
    template_env = template_env
    selected_templates = choose_prompt_templates(request)

    for template in selected_templates:
        prompt += render_template(template )

    if input_lang != DEFAULT_LANG and input_lang != UNDEFINED_LANG:
        prompt = translate_text(prompt, input_lang)

    prompt += template_env.get_template("messages.md").render(
        previous_messages=request["previous_messages"],
    )

    prompt += template_env.get_template("suggestion.md").render(
        my_name=request["settings"]["profile_params"]["name"],
    )

    return prompt

