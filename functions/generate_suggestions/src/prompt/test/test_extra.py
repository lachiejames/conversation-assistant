from ...test.mocks import EMPTY_REQUEST, EMPTY_REQUEST_WITH_NAMES
from ..extra import render_extra_template


def test_render_extra_template__when_all_extras_given__then_return_string_with_all_extras() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"

    result = render_extra_template(request)
    expected_result = """Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.
"""
    assert result == expected_result


def test_render_extra_template__when_no_names_given__then_return_string_with_no_names() -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"

    result = render_extra_template(request)
    expected_result = """I am 27 years old.
My pronouns are he/him.
I live in Camberwell, Victoria, Australia.
My occupation is Software Engineer.
My hobbies include coding, hanging out with my dog.
People describe me as a cool guy who always knows the right thing to say.
"""
    assert result == expected_result


def test_render_extra_template__when_nothing_given__then_return_string_with_no_params() -> None:
    request = EMPTY_REQUEST.copy()

    result = render_extra_template(request)
    expected_result = ""
    assert result == expected_result
