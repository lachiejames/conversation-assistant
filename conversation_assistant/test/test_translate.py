from unittest.mock import MagicMock, patch

from conversation_assistant.test.mocks import MOCK_TRANSLATION_RESPONSE, MOCK_DETECT_LANG_RESPONSE

from ..translate import detect_input_lang, translate_text


@patch("conversation_assistant.translate.Client.detect_language", MagicMock(return_value=MOCK_DETECT_LANG_RESPONSE))
def test_detect_input_lang__when_1_lang_returned__then_return_that_lang() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    it_text = detect_input_lang(text=en_text)
    assert it_text == "en"


@patch("conversation_assistant.translate.Client.translate", MagicMock(return_value=MOCK_TRANSLATION_RESPONSE))
def test_translate_text__when_en_to_it__then_translates_text_correctly() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    it_text = translate_text(text=en_text, target_lang="it")
    assert it_text == "Johnson, avresti dovuto pubblicare quel film ieri. Cosa sta succedendo?"


def test_translate_text__when_en_to_en__then_text_is_the_same() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    trans_en_text = translate_text(text=en_text, target_lang="en")
    assert en_text == trans_en_text


def test_translate_text__when_text_is_empty__then_returns_empty_string() -> None:
    empty_text = ""
    trans_empty_text = translate_text(text=empty_text, target_lang="en")
    assert empty_text == trans_empty_text


def test_translate_text__when_text_is_large__then_returns_large_text() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    large_en_text = en_text * 100
    large_it_text = translate_text(text=large_en_text, target_lang="it")
    assert len(large_it_text) > 1000
