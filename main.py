from conversation_assistant import run_generate_suggestions

import functions_framework  # type: ignore


@functions_framework.http
def generate_suggestions(request):
    return run_generate_suggestions(request)
