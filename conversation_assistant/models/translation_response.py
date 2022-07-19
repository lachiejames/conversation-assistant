from typing_extensions import TypedDict

TranslateResponse = TypedDict(
    "TranslateResponse",
    {
        "translatedText": str,
    },
)

DetectLangResponse = TypedDict(
    "DetectLangResponse",
    {
        "language": str,
        "confidence": int,
        "input": "str",
    },
)
