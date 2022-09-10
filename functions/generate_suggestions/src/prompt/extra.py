from ..utils import is_not_empty

INTRO_PATH = "extra"

def select_extra_templates(hobbies: str, self_description: str) -> list[str]:
    extra_templates = []

    if is_not_empty(hobbies):
        extra_templates.append(f"{INTRO_PATH}/hobbies.md")
    elif is_not_empty(self_description):
        extra_templates.append(f"{INTRO_PATH}/self_description.md")

    return extra_templates
