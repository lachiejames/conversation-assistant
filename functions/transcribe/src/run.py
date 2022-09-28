import json
from typing import Any, Union

from flask import Response


def run_generate_suggestions(request_body: Union[Any, None]) -> Response:
    return Response(
        response=json.dumps({"body": "What's crackin"}),
        status=200,
        headers={
            "Content-Type": "application/json",
        },
    )
