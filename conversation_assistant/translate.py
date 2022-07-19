import six
from google.cloud import translate_v2 as translate

from .models import DetectLangResponse, TranslateResponse


def detect_input_lang(text: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    response: DetectLangResponse = translate.Client().detect_language(text)
    detected_lang = response["language"]

    if isinstance(detected_lang, str):
        return detected_lang
    if isinstance(detected_lang, list) and len(detected_lang) > 0:
        return detected_lang[0]
    raise Exception(f"Failed to detect language: {response}")


def translate_text(text: str, target_lang: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    response: TranslateResponse = translate.Client().translate(text, target_language=target_lang)
    translated_text: str = response["translatedText"]

    if isinstance(translated_text, str):
        return translated_text

    raise Exception(f"Failed to translate: {response}")
