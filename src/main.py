import os

import openai
from openai.api_resources.completion import Completion

PROMPT = "mine was good.  I just had a lazy day today\n"
ENGINE = "davinci-instruct-beta"


def set_api_key() -> None:
    openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_question(question: str) -> str:
    response = openai.Completion.create(
        prompt=question,
        engine=ENGINE,
        temperature=0,
        top_p=1,
    )

    return response.choices[0].text


def run():
    print(f"Question - {PROMPT}")

    for i in range(10):
        response = ask_question(PROMPT)
        print(f"\n\n\n\n\n\n\n\n\n\n\n\nResponse #{i} - {response}")
