from ...test.mocks import MOCK_REQUEST, MOCK_REQUEST_NO_NAMES, MOCK_REQUEST_NOTHING
from ..suggestion import render_suggestion_template


def test_render_suggestion_template__when_names_given__then_return_string_with_names() -> None:
    result = render_suggestion_template(MOCK_REQUEST)
    expected_result = """
Chad Johnson:"""
    assert result == expected_result


def test_render_suggestion_template__when_no_names_given__then_return_string_without_names() -> None:
    result = render_suggestion_template(MOCK_REQUEST_NO_NAMES)
    expected_result = """
Me:"""
    assert result == expected_result


def test_render_suggestion_template__when_nothing_given__then_return_string_without_vars() -> None:
    result = render_suggestion_template(MOCK_REQUEST_NOTHING)
    expected_result = """
Me:"""
    assert result == expected_result
