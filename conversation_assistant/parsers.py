from .models import (
    ConversationParams,
    GPT3CompletionResponse,
    Message,
    ProfileParams,
    Suggestion,
)


def generate_prompt(profile_params: ProfileParams, conversation_params: ConversationParams, previous_messages: list[Message]) -> str:
    my_name: str = profile_params["name"]
    my_age: int = profile_params["age"]
    my_pronouns: str = profile_params["pronouns"]
    my_location: str = profile_params["location"]
    my_occupation: str = profile_params["occupation"]
    my_traits: str = ", ".join(profile_params["traits"])
    my_hobbies: str = ", ".join(profile_params["hobbies"])

    their_name: str = conversation_params["their_name"]
    their_relationship_to_me: str = conversation_params["their_relationship_to_me"]
    tone_of_chat: str = ", ".join(conversation_params["tone_of_chat"])

    prompt = f"""
The following is a conversation between {my_name} and {their_name}, who is {my_name}'s {their_relationship_to_me}.  
{my_name} is a {my_age} year old {my_occupation} who lives in {my_location}.
{my_name}'s pronouns are {my_pronouns}.
{my_name}'s favourite hobbies include {my_hobbies}.  
{my_name} can be described as {my_traits}.  
The tone of this conversation is {tone_of_chat}.

"""

    for message in previous_messages:
        prompt += f"{message['author']}: {message['text']}\n"

    # Generate the next message from the perspective of the 'me' (the user)
    prompt += f"{my_name}:"

    return prompt


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].lstrip()
        suggestions.append({"text": suggestion})

    return suggestions
