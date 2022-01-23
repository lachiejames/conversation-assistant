from jsonschema import ValidationError

import conversation_assistant.generator
from conversation_assistant.models import LambdaEvent, LambdaResponse, Suggestion
from conversation_assistant.validators import validate_message_suggestions


def respond_with_200(event: LambdaEvent) -> LambdaResponse:
    suggestions: list[Suggestion] = conversation_assistant.generator.generate_message_suggestions(event)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": {"results": suggestions},
    }


def respond_with_400(error: ValidationError) -> LambdaResponse:
    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": f"Error - Invalid event\nerror={error.message}",
    }


def respond_with_500(error: Exception) -> LambdaResponse:
    print(error)

    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": "Error - Something went wrong",
    }


def lambda_response(event: LambdaEvent) -> LambdaResponse:
    try:

        try:
            validate_message_suggestions(event)
        except ValidationError as error:
            return respond_with_400(error)

        return respond_with_200(event)

    except Exception as error:
        return respond_with_500(error)
