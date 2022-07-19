from typing import Any

import six
from google.cloud import translate_v2 as translate


def translate_text(text: str, target_lang: str) -> str:
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    translate_client = translate.Client()
    result: Any = translate_client.translate(text, target_language=target_lang)
    translated_text: Any = result["translatedText"]

    if isinstance(translated_text, str):
        return translated_text

    input_lang = result["detectedSourceLanguage"]
    raise Exception(f"Translation from '{input_lang}' to '{target_lang}'", result)
