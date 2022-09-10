from ..utils import is_not_empty


def select_intro_template(my_name: str, their_name: str) -> str:
    if is_not_empty(my_name) and is_not_empty(their_name):
        return "intro/complete.md"
    else:
        return "intro/no_names.md"
