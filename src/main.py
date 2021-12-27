import os
import openai


def set_api_key() -> None:
    openai.api_key = os.getenv("OPENAI_API_KEY")


def ask_question(question: str) -> str:
    return openai.Completion.create(
        prompt=question,
        engine="davinci-instruct-beta",
        temperature=0.1,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )


response = ask_question("hey, how are you?")

print(response)
