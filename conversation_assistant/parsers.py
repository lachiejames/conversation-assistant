from conversation_assistant.models import GPT3CompletionResponse, Message, Suggestion

LEADING_PROMPT = "Me: "
OPENING_PROMPT = "The following is a conversation between myself and <insert name>. The assistant is giving me tips for things to say."


def map_messages_to_prompt(messages: list[Message]) -> str:
    prompt = f"{OPENING_PROMPT}\n\n"

    for message in messages:
        prompt += f"{message['author']}: {message['text']}\n"

    # Ensures the suggested messages are from my perspective
    prompt += LEADING_PROMPT

    return prompt


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].lstrip()
        suggestions.append({"text": suggestion})

    return suggestions
