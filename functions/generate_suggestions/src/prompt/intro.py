from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix, is_not_empty
from .render import render_template

INTRO_PATH = "intro"


def select_intro_template(path_prefix: str, their_relationship_to_me: str, tone_of_chat: str) -> str:
    if is_not_empty(their_relationship_to_me) and is_not_empty(tone_of_chat):
        return f"{path_prefix}/default.md"
    return f"{path_prefix}/nothing.md"


def render_intro_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_intro_template(
        path_prefix=f"{choose_path_prefix(request)}/intro",
        their_relationship_to_me=request["settings"]["conversation_params"]["their_relationship_to_me"],
        tone_of_chat=request["settings"]["conversation_params"]["tone_of_chat"],
    )
    return render_template(request, selected_template)
