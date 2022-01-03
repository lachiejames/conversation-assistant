from conversation_assistant.gpt3 import fetch_completetion
from conversation_assistant.models import (
    GPT3CompletionResponse,
    LambdaEvent,
    Suggestion,
)
from conversation_assistant.parsers import (
    map_completion_response_to_suggestions,
    map_messages_to_prompt,
)


def generate_message_suggestions(event: LambdaEvent):
    prompt: str = map_messages_to_prompt(event["previous_messages"])
    completion_response: GPT3CompletionResponse = fetch_completetion(prompt, event["gpt3_params"])
    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)

    return suggestions
