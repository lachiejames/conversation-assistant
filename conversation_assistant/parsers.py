from .translate import translate_text
from .models import (
    GenerateSuggestionsRequest,
    GPT3CompletionResponse,
    Message,
    Suggestion,
)


def generate_prompt(request: GenerateSuggestionsRequest,input_lang:str) -> str:
    my_name: str = request["settings"]["profile_params"]["name"]
    my_age: str = request["settings"]["profile_params"]["age"]
    my_pronouns: str = request["settings"]["profile_params"]["pronouns"]
    my_location: str = request["settings"]["profile_params"]["location"]
    my_occupation: str = request["settings"]["profile_params"]["occupation"]
    my_hobbies: str = request["settings"]["profile_params"]["hobbies"]
    my_self_description: str = request["settings"]["profile_params"]["self_description"]

    their_name: str = request["settings"]["conversation_params"]["their_name"]
    their_relationship_to_me: str = request["settings"]["conversation_params"]["their_relationship_to_me"]
    tone_of_chat: str = request["settings"]["conversation_params"]["tone_of_chat"]

    previous_messages: list[Message] = request["previous_messages"]

    prompt = f"""
The following is a conversation between {my_name} and {their_name}, who is {my_name}'s {their_relationship_to_me}.
{my_name} is a {my_age} year old {my_occupation} who lives in {my_location}.
{my_name}'s pronouns are {my_pronouns}.
{my_name}'s favourite hobbies include {my_hobbies}.
{my_name} can be described as {my_self_description}.
The tone of this conversation is {tone_of_chat}.

"""
    
    translated_prompt: str = translate_text(prompt, input_lang)
    
    for message in previous_messages:
        translated_prompt += f"{message['author']}: {message['text']}\n"
    
    # Generate the next message from the perspective of the 'me' (the user)
    translated_prompt += f"{my_name}:"

    return translated_prompt


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].strip()
        suggestions.append({"text": suggestion})

    return suggestions
