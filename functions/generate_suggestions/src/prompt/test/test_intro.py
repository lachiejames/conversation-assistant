from src.test.mocks.requests import EMPTY_REQUEST_WITH_NAMES
from ...test.mocks import EMPTY_REQUEST
from ..intro import render_intro_template


def test_render_intro_template__when_names_and_tone_and_relationship_given__then_include_them() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Casual"

    result = render_intro_template(request)
    expected_result = "The following is a Casual conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.\n"
    assert result == expected_result


def test_render_intro_template__when_tone_and_relationship_but_no_names_given__then_include_them() -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Casual"

    result = render_intro_template(request)
    expected_result = "The following is a Casual conversation that I had with my Friend.\n"
    assert result == expected_result


def test_render_intro_template__when_nothing_given__then_return_string_without_vars() -> None:
    request = EMPTY_REQUEST.copy()

    result = render_intro_template(request)
    expected_result = "The following is a conversation that I had.\n"
    assert result == expected_result
