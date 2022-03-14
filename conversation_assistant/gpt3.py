from openai import Completion

from .models import GPT3CompletionResponse, GPT3Params


def fetch_completion(prompt: str, gpt3_params: GPT3Params, api_key: str) -> GPT3CompletionResponse:
    response: GPT3CompletionResponse = Completion.create(
        prompt=prompt,
        api_key=api_key,
        engine="davinci-instruct-beta-v3",
        temperature=gpt3_params["temperature"],
        n=gpt3_params["n"],
        max_tokens=gpt3_params["max_tokens"],
        best_of=gpt3_params["best_of"],
        top_p=gpt3_params["top_p"],
        frequency_penalty=["frequency_penalty"],
        presence_penalty=["presence_penalty"],
        stop=["stop"],
    )

    return response
