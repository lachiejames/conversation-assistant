from ...models import Suggestion
from ...test.mocks import MOCK_REQUEST_NO_NAMES, MOCK_REQUEST,MOCK_REQUEST_NOTHING
from ..extra import render_extra_template

def test_render_extra_template__when_all_extras_given__then_return_string_with_all_extras() -> None:
    result = render_extra_template(MOCK_REQUEST)
    expected_result = """Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include .
People describe Chad Johnson as a cool guy who always knows the right thing to say.
"""
    assert result == expected_result

def test_render_extra_template__when_no_names_given__then_return_string_with_no_names() -> None:
    result = render_extra_template(MOCK_REQUEST_NO_NAMES)
    expected_result = """I am 27 years old.
My pronouns are he/him.
I live in Camberwell, Victoria, Australia.
My occupation is Software Engineer.
My hobbies include coding, hanging out with my dog.
People describe me as a cool guy who always knows the right thing to say.
"""
    assert result == expected_result

def test_render_extra_template__when_nothing_given__then_return_string_with_no_params() -> None:
    result = render_extra_template(MOCK_REQUEST_NOTHING)
    expected_result = "\n"
    assert result == expected_result
