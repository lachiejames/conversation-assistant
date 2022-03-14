from typing import TypedDict

ProfileParams = TypedDict(
    "ProfileParams",
    {
        "name": str,
        "pronouns": str,
        "location": str,
        "occupation": str,
        "hobbies": list[str],
        "traits": list[str],
    },
)
