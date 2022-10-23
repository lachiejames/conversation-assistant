from ...test.mocks import EMPTY_REQUEST, EMPTY_REQUEST_WITH_NAMES
from ..suggestion import render_suggestion_template


def test_render_suggestion_template__when_no_names_given__then_return_no_name() -> None:
    request = EMPTY_REQUEST.copy()
    result = render_suggestion_template(request)
    expected_result = """
Me:"""
    assert result == expected_result


def test_render_suggestion_template__when_names_given__then_return_name() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    result = render_suggestion_template(request)
    expected_result = """
Chad Johnson:"""
    assert result == expected_result


def test_render_suggestion_template__when_rephrase_and_no_names_given__then_return_comment_and_no_name() -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Sup Stace, what's crack-a-lackin?"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Professional"

    result = render_suggestion_template(request)
    expected_result = """
Sup Stace, what's crack-a-lackin?

<Rephrase my message so that it sounds more Professional>

Me:"""
    assert result == expected_result


def test_render_suggestion_template__when_rephrase_and_tone_and_names_given__then_return_comment_and_name() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Sup Stace, what's crack-a-lackin?"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Professional"

    result = render_suggestion_template(request)
    expected_result = """
Sup Stace, what's crack-a-lackin?

<Rephrase Chad Johnson's message so that it sounds more Professional>

Chad Johnson:"""
    assert result == expected_result
