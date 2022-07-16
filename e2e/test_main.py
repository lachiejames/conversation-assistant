import json
import os
from typing import Any, List

import flask
import pytest
from conversation_assistant.models import GenerateMessageSuggestionsRequest, LambdaResponse, Suggestion

from main import generate_suggestions
import requests


# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app() -> flask.Flask:
    return flask.Flask(__name__)


def get_path_to_file(filename: str) -> str:
    return os.path.abspath(os.path.join(__file__, "..", "mock_requests", filename))


def test_generate_suggestions__when_valid_request_received__then_returns_1_suggestion(app: flask.Flask):
    with open(get_path_to_file("tinder.json"), "r", encoding="utf-8") as example_request_file:
        with app.test_request_context(json=json.load(example_request_file)):
            response: LambdaResponse = generate_suggestions(flask.request)

            parsed_response: Any = json.loads(response["body"])
            suggestions: List[Suggestion] = parsed_response["results"]

            assert len(suggestions) == 1
