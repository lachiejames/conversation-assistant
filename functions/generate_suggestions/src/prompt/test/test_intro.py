from ...models import Suggestion
from ...test.mocks import MOCK_REQUEST, MOCK_REQUEST_NO_NAMES, MOCK_REQUEST_NOTHING
from ..intro import render_intro_template


def test_render_intro_template__when_names_given__then_return_string_with_names() -> None:
    result = render_intro_template(MOCK_REQUEST)
    expected_result = "The following is a casual conversation between Chad Johnson and Stacey, who is Chad Johnson's friend.\n"
    assert result == expected_result


def test_render_intro_template__when_no_names_given__then_return_string_without_names() -> None:
    result = render_intro_template(MOCK_REQUEST_NO_NAMES)
    expected_result = "The following is a casual conversation that I had with my friend.\n"
    assert result == expected_result


def test_render_intro_template__when_nothing_given__then_return_string_without_vars() -> None:
    result = render_intro_template(MOCK_REQUEST_NOTHING)
    expected_result = "The following is a conversation that I had.\n"
    assert result == expected_result
