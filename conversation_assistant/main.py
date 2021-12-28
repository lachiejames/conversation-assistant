import os

import openai
from openai import Completion

PROMPT = """
Human - Hello, how are you today?,
Bot - Hi I am good.  I am 45, how old are you?,
Human - I am 30, what do you do for work?,
Bot - I work in the city where I live.  What do you do for work?
"""
PROMPTS = [
    "Human - Hello, how are you today?",
    "Bot - Hi I am good.  I am 45, how old are you?",
    "Human - I am 30, what do you do for work?",
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
    print(f"Question - {PROMPT}")

    choices = get_responses_to_prompts(PROMPTS)
    log_responses(choices)


run()
