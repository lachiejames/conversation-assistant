from typing import Any

import six
from google.cloud import translate_v2 as translate


def translate_text(text: str, target_lang: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    translate_client = translate.Client()
    result: Any = translate_client.translate(text, target_language=target_lang)
    input_lang = result["detectedSourceLanguage"]
    translated_text: Any = result["translatedText"]

    print(f"Translated from {input_lang} to {target_lang}\ntext='{text}'\ntranslated_text='{translated_text}'")

    if isinstance(translated_text, str):
        return translated_text

    raise Exception(f"Failed to translate: {result}")
