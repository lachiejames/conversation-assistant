from conversation_assistant.models.gpt3_completion_response import GPT3CompletionResponse
from conversation_assistant.models.message import Message
from conversation_assistant.models.suggestion import Suggestion
from conversation_assistant.parsers import (
    map_completion_response_to_suggestions,
    map_messages_to_prompt,
)
from conversation_assistant.gpt3 import fetch_completetion


def generate_message_suggestions(previous_messages: list[Message]):
    prompt: str = map_messages_to_prompt(previous_messages)
    completion_response: GPT3CompletionResponse = fetch_completetion(prompt)
    suggestions: list[Suggestion] = map_completion_response_to_suggestions(completion_response)

    return suggestions
