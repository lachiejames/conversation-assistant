import flask

import main

app = flask.Flask(__name__)


@app.route("/generate-suggestions-function", methods=["POST"])
def generate() -> flask.Response:
    return main.transcribe(flask.request)
