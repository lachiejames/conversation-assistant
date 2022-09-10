from ..models import GenerateSuggestionsRequest, Message
from ..utils import choose_path_prefix
from .render import render_template


def select_message_template(path_prefix: str, previous_messages: list[Message]) -> str:
    are_messages_given = len(previous_messages) > 0

    if are_messages_given:
        return f"{path_prefix}/default.md"
    return f"{path_prefix}/no_messages.md"


def render_message_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_message_template(
        path_prefix=f"{choose_path_prefix(request)}/message",
        previous_messages=request["previous_messages"],
    )
    return render_template(request, selected_template)
