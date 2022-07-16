from typing_extensions import TypedDict

from .conversation_params import ConversationParams
from .gpt3_params import GPT3Params
from .message import Message
from .profile_params import ProfileParams

Settings = TypedDict(
    "Settings",
    {
        "conversation_params": ConversationParams,
        "profile_params": ProfileParams,
        "gpt3_params": GPT3Params,
    },
)

GenerateMessageSuggestionsRequest = TypedDict(
    "GenerateMessageSuggestionsRequest",
    {
        "previous_messages": list[Message],
        "settings": Settings,
    },
)
