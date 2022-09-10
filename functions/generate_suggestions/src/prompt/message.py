from ..models import GenerateSuggestionsRequest
from ..utils import is_not_empty
from .render import render_template

MESSAGE_PATH = "message"


def select_message_template(my_name: str, their_name: str) -> str:
    if is_not_empty(my_name) and is_not_empty(their_name):
        return f"{MESSAGE_PATH}/complete.md"
    return f"{MESSAGE_PATH}/no_names.md"


def render_message_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_message_template(
        my_name=request["settings"]["profile_params"]["name"],
        their_name=request["settings"]["conversation_params"]["their_name"],
    )
    return render_template(request, selected_template)
