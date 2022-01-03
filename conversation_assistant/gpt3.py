import os

from openai import Completion

from conversation_assistant.models import GPT3CompletionResponse


def fetch_completetion(prompt: str) -> GPT3CompletionResponse:
    return Completion.create(
        prompt=prompt,
        api_key=os.getenv("OPENAI_API_KEY"),
        engine="davinci-instruct-beta-v3",
        temperature=0.7,
        n=3,
        max_tokens=50,
    )
