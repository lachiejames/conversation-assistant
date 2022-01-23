import os

from openai import Completion

from conversation_assistant.models import GPT3CompletionResponse, GPT3Params


def fetch_completion(prompt: str, gpt3_params: GPT3Params) -> GPT3CompletionResponse:
    return Completion.create(
        prompt=prompt,
        api_key=os.getenv("OPENAI_API_KEY"),
        engine="davinci-instruct-beta-v3",
        temperature=gpt3_params["randomness"],
        n=gpt3_params["num_results"],
        max_tokens=gpt3_params["max_length"],
    )
