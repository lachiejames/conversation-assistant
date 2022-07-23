import flask


app = flask.Flask(__name__)
from conversation_assistant import main

@app.route("/", methods=["POST"])
def generate() -> flask.Response:
    return main.generate_suggestions(flask.request)
