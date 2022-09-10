from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix
from .render import render_template

INTRO_PATH = "intro"


def select_intro_template(path_prefix: str) -> str:
    return f"{path_prefix}/default.md"


def render_intro_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_intro_template(
        path_prefix=f"{choose_path_prefix(request)}/intro",
    )
    return render_template(request, selected_template)
