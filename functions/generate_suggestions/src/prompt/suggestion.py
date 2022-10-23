from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix
from .render import render_template


def select_suggestion_template(path_prefix: str, should_rephrase: bool) -> str:
    if should_rephrase:
        return f"{path_prefix}/rephrase.md"
    return f"{path_prefix}/default.md"


def render_suggestion_template(request: GenerateSuggestionsRequest) -> str:
    message_to_rephrase = request["settings"]["conversation_params"].get("message_to_rephrase", "")
    selected_template = select_suggestion_template(
        path_prefix=f"{choose_path_prefix(request)}/suggestion",
        should_rephrase=bool(message_to_rephrase),
    )
    return render_template(request, selected_template)
