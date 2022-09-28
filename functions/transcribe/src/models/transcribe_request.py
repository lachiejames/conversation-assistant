from typing_extensions import TypedDict

TranscribeRequest = TypedDict(
    "TranscribeRequest",
    {
        "uid": str,
        "audio_data": str,
    },
)
