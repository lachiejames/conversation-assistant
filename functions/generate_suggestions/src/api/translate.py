import six
from google.cloud.translate_v2.client import Client

from ..models import DetectLangResponse, TranslateResponse

UNDEFINED_LANG = "und"


def detect_input_lang(text: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    response: DetectLangResponse = Client().detect_language(text)
    detected_lang = response["language"]

    if detected_lang != UNDEFINED_LANG:
        return detected_lang
    raise ValueError(f"Failed to detect language: {response}")


def translate_text(text: str, target_lang: str) -> str:
    """
    Depends on GOOGLE_APPLICATION_CREDENTIALS environment variable, which must point to a
    valid Google Cloud Service Account JSON file
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    response: TranslateResponse = Client().translate(text, target_language=target_lang)
    translated_text: str = response["translatedText"]

    return translated_text
