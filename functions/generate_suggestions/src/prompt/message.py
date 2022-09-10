from ..utils import is_not_empty

MESSAGE_PATH = "message"


def select_message_template(my_name: str, their_name: str) -> str:
    if is_not_empty(my_name) and is_not_empty(their_name):
        return f"{MESSAGE_PATH}/complete.md"
    else:
        return f"{MESSAGE_PATH}/no_names.md"
