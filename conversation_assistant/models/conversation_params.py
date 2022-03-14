from typing import TypedDict
from .message import Message

ConversationParams = TypedDict(
    "ConversationParams",
    {
        "names": list[str],
        "relationship": str,
        "tone": str,
        "previous_messages": list[Message],
    },
)
