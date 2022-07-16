from conversation_assistant import run_lambda

import functions_framework  # type: ignore


@functions_framework.http
def generate_suggestions(request):
    return run_lambda(request)
