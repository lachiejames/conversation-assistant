from typing import TypedDict

from .message import Message

ConversationParams = TypedDict(
    "ConversationParams",
    {
        "their_name": str,
        "their_relationship_to_me": str,
        "tone_of_chat": str,
        "previous_messages": list[Message],
    },
)
