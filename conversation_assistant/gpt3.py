import os

from openai import Completion

from conversation_assistant.validators import validate_completion_response

from .models import GPT3CompletionResponse, GPT3Params


def fetch_completion(prompt: str, gpt3_params: GPT3Params) -> GPT3CompletionResponse:
    response: GPT3CompletionResponse = Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt=prompt,
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=gpt3_params["temperature"],
        n=gpt3_params["n"],
        max_tokens=gpt3_params["max_tokens"],
        best_of=gpt3_params["best_of"],
        top_p=gpt3_params["top_p"],
        frequency_penalty=gpt3_params["frequency_penalty"],
        presence_penalty=gpt3_params["presence_penalty"],
        stop=gpt3_params["stop"],
    )

    validate_completion_response(response)

    return response
