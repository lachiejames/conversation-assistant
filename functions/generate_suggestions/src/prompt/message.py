from ..models import GenerateSuggestionsRequest, Message
from ..utils import is_not_empty
from .render import render_template

MESSAGE_PATH = "message"


def select_message_template(my_name: str, their_name: str, previous_messages: list[Message]) -> str:
    are_names_given = is_not_empty(my_name) and is_not_empty(their_name)
    are_messages_given = len(previous_messages) > 0

    if are_names_given and are_messages_given:
        return f"{MESSAGE_PATH}/complete.md"
    if are_messages_given:
        return f"{MESSAGE_PATH}/no_names.md"
    return f"{MESSAGE_PATH}/nothing.md"


def render_message_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_message_template(
        my_name=request["settings"]["profile_params"]["name"],
        their_name=request["settings"]["conversation_params"]["their_name"],
        previous_messages=request["previous_messages"],
    )
    return render_template(request, selected_template)
