import flask

import main


app = flask.Flask(__name__)


@app.route("/")
def index():
    return main.generate_suggestions(flask.request)
