from typing_extensions import TypedDict

Message = TypedDict(
    "Message",
    {
        "text": str,
        "author": str,
    },
)
