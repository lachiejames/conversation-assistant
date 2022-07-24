# pylint: disable=unused-import
from .generator import fetch_suggestions
from .gpt3 import fetch_completion
from .parsers import generate_prompt, map_completion_response_to_suggestions
from .translate import detect_input_lang, translate_text
