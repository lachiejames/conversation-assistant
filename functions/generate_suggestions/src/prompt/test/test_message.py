from ...test.mocks import EMPTY_REQUEST, EMPTY_REQUEST_WITH_NAMES
from ..message import render_message_template


def test_render_message_template__when_names_and_relationship_and_messages_given__then_return_messages_with_names() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    result = render_message_template(request)
    expected_result = """
Stacey: Hey Chad!

Chad Johnson: What's crackin babydoll

Stacey: I think I'm pregnant...
"""
    assert result == expected_result


def test_render_message_template__when_relationship_and_messages_but_no_names_given__then_return_messages_with_relationship() -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    result = render_message_template(request)
    expected_result = """
Friend: Hey Chad!

Me: What's crackin babydoll

Friend: I think I'm pregnant...
"""
    assert result == expected_result


def test_render_message_template__when_messages_but_no_names_no_relationship_given__then_return_messages_with_no_names() -> None:
    request = EMPTY_REQUEST.copy()
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    result = render_message_template(request)
    expected_result = """
Them: Hey Chad!

Me: What's crackin babydoll

Them: I think I'm pregnant...
"""
    assert result == expected_result


def test_render_message_template__when_names_and_relationship_but_no_messages_given__then_return_nothing() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"

    result = render_message_template(request)
    expected_result = ""
    assert result == expected_result


def test_render_message_template__when_nothing_given__then_return_nothing() -> None:
    request = EMPTY_REQUEST.copy()

    result = render_message_template(request)
    expected_result = ""
    assert result == expected_result