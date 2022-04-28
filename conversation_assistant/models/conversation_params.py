from typing import TypedDict

ConversationParams = TypedDict(
    "ConversationParams",
    {
        "their_name": str,
        "their_relationship_to_me": str,
        "tone_of_chat": str,
    },
)
