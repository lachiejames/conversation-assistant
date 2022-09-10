from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix
from .render import render_template


def select_suggestion_template(path_prefix: str) -> str:
    return f"{path_prefix}/default.md"


def render_suggestion_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_suggestion_template(
        path_prefix=f"{choose_path_prefix(request)}/suggestion",
    )
    return render_template(request, selected_template)
