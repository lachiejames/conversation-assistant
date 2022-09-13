from ..models import GenerateSuggestionsRequest
from ..utils import DEFAULT_LANG, UNDEFINED_LANG, translate_text
from .extra import render_extra_template
from .intro import render_intro_template
from .message import render_message_template
from .suggestion import render_suggestion_template


def construct_prompt(request: GenerateSuggestionsRequest, input_lang: str) -> str:
    prompt = ""
    prompt += render_intro_template(request)
    prompt += render_extra_template(request)

    # By default, the prompt intro/extra stages are in English.  If a different language is detected
    # in the previous_messages, the intro/extra stages will be translated to that language.
    if input_lang not in (DEFAULT_LANG, UNDEFINED_LANG):
        prompt = translate_text(prompt, input_lang)

    prompt += render_message_template(request)
    prompt += render_suggestion_template(request)

    return prompt
