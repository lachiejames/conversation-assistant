from ..models import GenerateSuggestionsRequest
from ..utils import choose_path_prefix
from .render import render_template


def select_suggestion_template(path_prefix: str, should_rephrase: bool) -> str:
    if should_rephrase:
        return f"{path_prefix}/rephrase.md"
    return f"{path_prefix}/default.md"


def render_suggestion_template(request: GenerateSuggestionsRequest) -> str:
    selected_template = select_suggestion_template(
        path_prefix=f"{choose_path_prefix(request)}/suggestion",
        should_rephrase=len(request["settings"]["conversation_params"]["message_to_rephrase"]) > 0,
    )
    return render_template(request, selected_template)


# def select_message_template(path_prefix: str, their_relationship_to_me: str, previous_messages: list[Message]) -> str:
#     are_names_given = path_prefix.startswith("names")
#     are_messages_given = len(previous_messages) > 0
#     is_their_relationship_to_me_given = is_not_empty(their_relationship_to_me)

#     if not are_messages_given:
#         return f"{path_prefix}/no_messages.md"
#     if are_names_given:
#         return f"{path_prefix}/default.md"
#     if is_their_relationship_to_me_given:
#         return f"{path_prefix}/relationship.md"
#     return f"{path_prefix}/nothing.md"


# def render_message_template(request: GenerateSuggestionsRequest) -> str:
#     selected_template = select_message_template(
#         path_prefix=f"{choose_path_prefix(request)}/message",
#         their_relationship_to_me=request["settings"]["conversation_params"]["their_relationship_to_me"],
#         previous_messages=request["previous_messages"],
#     )
#     return render_template(request, selected_template)
