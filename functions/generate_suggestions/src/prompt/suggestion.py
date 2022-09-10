from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix
from .render import render_template


def select_suggestion_template(path_prefix: str) -> str:
    return f"{path_prefix}/suggestion/default.md"


def render_suggestion_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_suggestion_template(
        path_prefix=choose_path_prefix(request),
    )
    return render_template(request, selected_template)
