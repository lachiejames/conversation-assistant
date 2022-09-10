from ..models import GenerateSuggestionsRequest
from ..utils import is_not_empty, has_names
from .render import render_template

INTRO_PATH = "intro"


def select_intro_template(has_names: bool) -> str:
    if has_names:
        return "names/default.md"
    return "no_names/default.md"


def render_intro_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_intro_template(
        has_names=has_names(request),
    )
    return render_template(request, selected_template)
