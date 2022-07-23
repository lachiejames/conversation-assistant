import flask

import main

app = flask.Flask(__name__)


@app.route("/", methods=["POST"])
def generate() -> flask.Response:
    return main.generate_suggestions(flask.request)
