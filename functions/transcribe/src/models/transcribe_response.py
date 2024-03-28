from typing_extensions import TypedDict

from .message import Message

TranscribeResponse = TypedDict(
    "TranscribeResponse",
    {
        "messages": list[Message],
    },
)
