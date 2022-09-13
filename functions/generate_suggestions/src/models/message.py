from typing_extensions import TypedDict

Message = TypedDict(
    "Message",
    {
        "text": str,
        "is_my_message": bool,
    },
)
