from typing import TypedDict

ProfileParams = TypedDict(
    "ProfileParams",
    {
        "name": str,
        "age": int,
        "pronoun": str,
        "location": str,
        "occupation": str,
        "hobbies": list[str],
        "traits": list[str],
    },
)
