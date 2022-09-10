from ..utils import is_not_empty

SUGGESTION_PATH = "suggestion"


def select_suggestion_template(my_name: str, their_name: str) -> str:
    if is_not_empty(my_name) and is_not_empty(their_name):
        return f"{SUGGESTION_PATH}/complete.md"
    else:
        return f"{SUGGESTION_PATH}/no_names.md"
