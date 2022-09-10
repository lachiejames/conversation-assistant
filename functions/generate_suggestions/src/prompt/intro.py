from ..utils import is_not_empty

INTRO_PATH = "intro"


def select_intro_template(my_name: str, their_name: str) -> str:
    if is_not_empty(my_name) and is_not_empty(their_name):
        return f"{INTRO_PATH}/complete.md"
    else:
        return f"{INTRO_PATH}/no_names.md"
