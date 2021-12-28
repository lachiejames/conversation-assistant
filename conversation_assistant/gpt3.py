from openai import Completion


def extract_suggestions(choices_response: list) -> list[str]:
    suggestions: list[str] = []

    for choice in choices_response:
        suggestions.append(choice.text.lstrip())

    return suggestions


def get_suggestions_for_next_message(chatlog: str) -> list[str]:
    gpt3_completion_response = Completion.create(
        prompt=chatlog,
        engine="davinci-instruct-beta-v3",
        temperature=0.7,
        n=3,
        max_tokens=50,
    )

    return extract_suggestions(gpt3_completion_response.choices)
