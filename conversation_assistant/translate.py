from typing import Any, Union

import six
from google.cloud import translate_v2 as translate


def detect_input_lang(text: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    translate_client = translate.Client()
    detected_lang: Union[str, list[str]] = translate_client.detect_language(text)

    if isinstance(detected_lang, str):
        return detected_lang
    elif type(detected_lang) == "list" and len(detected_lang) > 0:
        return detected_lang[0]
    raise Exception(f"Failed to detect language: {detected_lang}")


def translate_text(text: str, target_lang: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    translate_client = translate.Client()
    result: Any = translate_client.translate(text, target_language=target_lang)
    translated_text: Any = result["translatedText"]

    if isinstance(translated_text, str):
        return translated_text

    raise Exception(f"Failed to translate: {result}")
