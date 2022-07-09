from typing import TypedDict

ProfileParams = TypedDict(
    "ProfileParams",
    {
        "name": str,
        "age": str,
        "pronouns": str,
        "location": str,
        "occupation": str,
        "hobbies": str,
        "self_description": str,
    },
)
