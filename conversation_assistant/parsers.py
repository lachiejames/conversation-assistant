from conversation_assistant.models import GPT3CompletionResponse, Message, Suggestion

LEADING_PROMPT = "Me: "


def generate_opening_prompt(messages: list[Message]) -> str:
    people_in_convo: list[str] = []

    for message in messages:
        if message["author"] not in people_in_convo:
            people_in_convo.append(message["author"])

    return f"""The following is a conversation between {people_in_convo}.
The assistant will give Me suggestions for things to say in this conversation.

"""


def map_messages_to_prompt(messages: list[Message]) -> str:
    prompt = generate_opening_prompt(messages)

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
