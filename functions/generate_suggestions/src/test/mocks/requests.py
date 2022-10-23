import copy

from ...models import GenerateSuggestionsRequest

EMPTY_REQUEST: GenerateSuggestionsRequest = {
    "uid": "",
    "previous_messages": [],
    "settings": {
        "profile_params": {
            "name": "",
            "age": "",
            "pronouns": "",
            "location": "",
            "occupation": "",
            "hobbies": "",
            "self_description": "",
        },
        "conversation_params": {
            "their_name": "",
            "their_relationship_to_me": "",
            "tone_of_chat": "",
            "message_to_rephrase": "",
        },
        "gpt3_params": {
            "engine": "text-davinci-002",
            "n": 1,
            "temperature": 1.0,
            "max_tokens": 50,
            "best_of": 1,
            "frequency_penalty": 1.0,
            "presence_penalty": 1.0,
        },
    },
}


EMPTY_REQUEST_WITH_NAMES = copy.deepcopy(EMPTY_REQUEST)
EMPTY_REQUEST_WITH_NAMES["settings"]["profile_params"]["name"] = "Chad Johnson"
EMPTY_REQUEST_WITH_NAMES["settings"]["conversation_params"]["their_name"] = "Stacey"
