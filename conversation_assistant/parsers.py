from openai import Completion

from conversation_assistant.models.gpt3_completion_response import (
    GPT3CompletionResponse,
)


def fetch_completetion(prompt: str) -> GPT3CompletionResponse:
    return Completion.create(
        prompt=prompt,
        engine="davinci-instruct-beta-v3",
        temperature=0.7,
        n=3,
        max_tokens=50,
    )
