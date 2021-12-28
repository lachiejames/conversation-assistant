import os

import openai
from openai import Completion

PROMPT = """
Ideas involving education and virtual reality

1. Virtual Mars
Students get to explore Mars via virtual reality and go on missions to collect and catalog what they see.
"""
PROMPTS = [
    "Hello, how are you today?",
]
ENGINE = "davinci-instruct-beta-v3"


def set_api_key() -> None:
    openai.api_key = os.getenv("OPENAI_API_KEY")


def get_responses_to_prompts(prompts: list[str]) -> list[str]:
    response = Completion.create(
        prompt=prompts, engine=ENGINE, temperature=0.7, n=3, max_tokens=50
    )

    list_of_responses = [choice.text for choice in response.choices]
    return list_of_responses


def log_responses(responses: list[str]):
    for response in responses:
        print(f"\n\n\nResponse - {response}")


def run():
    print(f"Question - {PROMPTS}")

    choices = get_responses_to_prompts(PROMPTS)
    log_responses(choices)


run()
