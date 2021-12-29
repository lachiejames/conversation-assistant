from conversation_assistant.models.gpt3_completion_response import GPT3CompletionResponse
from conversation_assistant.models.message import Message
from conversation_assistant.models.suggestion import Suggestion

LEADING_PROMPT = "Me - "


def parse_message_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestions.append({"text": choice["text"].lstrip()})

    return suggestions


def map_messages_to_prompt(messages: list[Message]) -> str:
    prompt = ""

    for message in messages:
        prompt += f"{message['author']} - {message['text']}\n"

    # Ensures the suggested messages are from my perspective
    prompt += LEADING_PROMPT

    return prompt
