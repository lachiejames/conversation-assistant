# import flask

# import main

# app = flask.Flask(__name__)


# @app.route("/generate-suggestions-function", methods=["POST"])
# def generate() -> flask.Response:
#     return main.generate_suggestions(flask.request)


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()