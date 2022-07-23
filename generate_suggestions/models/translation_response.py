from typing_extensions import TypedDict

TranslateResponse = TypedDict(
    "TranslateResponse",
    {
        "translatedText": str,
        "detectedSourceLanguage": str,
        "input": str,
    },
)

DetectLangResponse = TypedDict(
    "DetectLangResponse",
    {
        "language": str,
        "input": str,
        "confidence": float,
    },
)
