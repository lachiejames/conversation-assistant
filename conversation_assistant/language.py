from typing import Any, Union

from translate import Translator


def translate_text(text: str, input_lang: str, output_lang: str) -> str:
    translator = Translator(from_lang=input_lang, to_lang=output_lang)
    result: Union[Any, str] = translator.translate(text)

    if isinstance(result, str):
        return result

    raise Exception(f"Translation from '{input_lang}' to '{output_lang}' failed\n\nText: ${text}\n\nResult:{result}")
