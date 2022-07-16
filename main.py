from dotenv import load_dotenv

from conversation_assistant import LambdaEvent, run_lambda


def generate_suggestions(request: LambdaEvent):
    load_dotenv(".env")
    return run_lambda(request)
# import flask

# def hello_name(request):
#     """HTTP Cloud Function.
#     Args:
#         request (flask.Request): The request object.
#         <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
#     Returns:
#         The response text, or any set of values that can be turned into a
#         Response object using `make_response`
#         <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
#     """
#     request_args = request.args

#     if request_args and "name" in request_args:
#         name = request_args["name"]
#     else:
#         name = "World"
#     return "Hello {}!".format(flask.escape(name))