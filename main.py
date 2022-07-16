from conversation_assistant import LambdaEvent, run_lambda


def generate_suggestions(request: LambdaEvent):
    return run_lambda(request)
