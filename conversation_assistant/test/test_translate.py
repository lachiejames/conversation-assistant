from ..language import translate_text

# NOTE: these tests make live requests to the Google Translate API


def test_translate_text__when_en_to_it__then_translates_text_correctly() -> None:
    en_text = "Johnson, you were supposed to have that feature out yesterday.  What is going on?"
    it_text = translate_text(text=en_text, input_lang="en", output_lang="it")
    assert it_text == "Johnson, avresti dovuto mostrare quel servizio ieri.  Cosa sta succedendo?"

