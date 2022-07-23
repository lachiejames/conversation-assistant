# Create a fake "app" for generating test request contexts.
import flask
import pytest


@pytest.fixture()
def app() -> flask.Flask:
    return flask.Flask(__name__)