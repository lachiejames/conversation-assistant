from typing import Optional

from typing_extensions import TypedDict

from .message import Message

ConversationParams = TypedDict(
    "ConversationParams",
    {
        "their_name": str,
        "their_relationship_to_me": str,
        "tone_of_chat": str,
        # Marked as optional to prevent breaking changes for Android users who haven't updated to the latest version of the app.
        "message_to_rephrase": Optional[str],
    },
)

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

GPT3Params = TypedDict(
    "GPT3Params",
    {
        "engine": str,
        "n": int,
        "temperature": float,
        "max_tokens": int,
        "best_of": int,
        "frequency_penalty": float,
        "presence_penalty": float,
    },
)


Settings = TypedDict(
    "Settings",
    {
        "conversation_params": ConversationParams,
        "profile_params": ProfileParams,
        "gpt3_params": GPT3Params,
    },
)

GenerateSuggestionsRequest = TypedDict(
    "GenerateSuggestionsRequest",
    {
        "uid": str,
        "previous_messages": list[Message],
        "settings": Settings,
    },
)
