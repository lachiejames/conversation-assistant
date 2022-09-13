from unittest.mock import MagicMock, patch

from ...models import DetectLangResponse, TranslateResponse
from .. import detect_input_lang, translate_text

MOCK_DETECT_LANG_SUCCESS_RESPONSE: DetectLangResponse = {
    "language": "en",
    "input": "Johnson, you were supposed to have that feature out yesterday.  What is going on?",
    "confidence": 0.99,
}

MOCK_DETECT_LANG_FAILURE_RESPONSE: DetectLangResponse = {"language": "und", "confidence": 1, "input": ""}

MOCK_TRANSLATION_RESPONSE: TranslateResponse = {
    "translatedText": "Johnson, avresti dovuto pubblicare quel film ieri. Cosa sta succedendo?",
    "detectedSourceLanguage": "en",
    "input": "Johnson, you were supposed to have that feature out yesterday.  What is going on?",
}


@patch("src.translate.Client.detect_language", MagicMock(return_value=MOCK_DETECT_LANG_SUCCESS_RESPONSE))
def test_detect_input_lang__when_valid_lang_received__then_return_that_lang() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    lang = detect_input_lang(text=en_text)
    assert lang == "en"


@patch("src.translate.Client.translate", MagicMock(return_value=MOCK_TRANSLATION_RESPONSE))
def test_translate_text__when_translation_received__then_returns_translated_text() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    it_text = translate_text(text=en_text, target_lang="it")
    assert it_text == "Johnson, avresti dovuto pubblicare quel film ieri. Cosa sta succedendo?"
