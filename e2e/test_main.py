import json
import os
from typing import Any, List
from unittest.mock import MagicMock, patch

import flask

from conversation_assistant.models import Suggestion
from main import generate_suggestions


def get_path_to_file(filename: str) -> str:
    return os.path.abspath(os.path.join(__file__, "..", "mock_requests", filename))


def test_generate_suggestions__when_valid_request_received__then_returns_1_suggestion(app: flask.Flask) -> None:
    with open(get_path_to_file("work.json"), "r", encoding="utf-8") as example_request_file:
        with app.test_request_context(json=json.load(example_request_file)):
            response: flask.Response = generate_suggestions(flask.request)

            parsed_response: Any = json.loads(response.data)
            suggestions: List[Suggestion] = parsed_response["results"]

            assert response.status_code == 200
            assert len(suggestions) == 1


def test_generate_suggestions__when_request_is_missing_required_properties__then_returns_400(app: flask.Flask) -> None:
    with app.test_request_context(json={"this": "will fail"}):
        response: flask.Response = generate_suggestions(flask.request)

        assert response.status_code == 400
        assert b"Invalid request body: 'previous_messages' is a required property" in response.data


def test_generate_suggestions__when_request_is_malformed__then_returns_400(app: flask.Flask) -> None:
    with app.test_request_context(data="this will fail"):
        response: flask.Response = generate_suggestions(flask.request)

        assert response.status_code == 400
        assert response.data == b"Invalid request body: Request body is required"


@patch("conversation_assistant.run.respond_with_200", MagicMock(side_effect=ImportError("test")))
def test_generate_suggestions__when_other_error_raised__then_returns_500(app: flask.Flask) -> None:
    with open(get_path_to_file("work.json"), "r", encoding="utf-8") as example_request_file:
        with app.test_request_context(json=json.load(example_request_file)):
            response: flask.Response = generate_suggestions(flask.request)

            assert response.status_code == 500
            assert response.data == b"Something went wrong: test"
