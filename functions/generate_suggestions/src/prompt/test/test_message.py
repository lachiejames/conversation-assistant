from ...models import Suggestion
from ...test.mocks import MOCK_REQUEST, MOCK_REQUEST_NO_NAMES, MOCK_REQUEST_NOTHING
from ..message import render_message_template


def test_render_message_template__when_names_and_messages_given__then_return_string_with_names() -> None:
    result = render_message_template(MOCK_REQUEST)
    expected_result = """
Stacey: Hey Chad!

Chad Johnson: What's crackin babydoll

Stacey: I think I'm pregnant...
"""
    assert result == expected_result


def test_render_message_template__when_names_and_no_messages_given__then_return_expected_string() -> None:
    result = render_message_template(MOCK_REQUEST)
    expected_result = ""
    assert result == expected_result


def test_render_message_template__when_no_names_and_messages_given__then_return_expected_string() -> None:
    result = render_message_template(MOCK_REQUEST_NO_NAMES)
    expected_result = """
Them: Hey Chad!

Me: What's crackin babydoll

Them: I think I'm pregnant...
"""
    assert result == expected_result


def test_render_message_template__when_no_names_and_no_messages_given__then_return_expected_string() -> None:
    result = render_message_template(MOCK_REQUEST_NO_NAMES)
    expected_result = "The following is a casual conversation that I had with my friend.\n"
    assert result == expected_result


def test_render_message_template__when_no_names_and_no_messages_given__then_return_expected_string() -> None:
    result = render_message_template(MOCK_REQUEST_NO_NAMES)
    expected_result = "The following is a casual conversation that I had with my friend.\n"
    assert result == expected_result


def test_render_message_template__when_nothing_given__then_return_expected_string() -> None:
    result = render_message_template(MOCK_REQUEST_NOTHING)
    expected_result = ""
    assert result == expected_result
