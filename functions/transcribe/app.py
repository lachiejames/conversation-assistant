import flask

import main

app = flask.Flask(__name__)


@app.route("/transcribe-function", methods=["POST"])
def transcribe() -> flask.Response:
    return main.transcribe(flask.request)
