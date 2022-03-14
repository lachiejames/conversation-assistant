from .models import (
    ConversationParams,
    GPT3CompletionResponse,
    ProfileParams,
    Suggestion,
)


def generate_prompt(profile_params: ProfileParams, conversationParams: ConversationParams) -> str:
    my_name = profile_params["name"]
    my_age = profile_params["age"]
    my_pronoun = profile_params["pronoun"]
    my_location = profile_params["location"]
    my_occupation = profile_params["occupation"]
    my_traits = profile_params["traits"]
    my_hobbies = profile_params["hobbies"]

    their_name = conversationParams["their_name"]
    their_relationship_to_me = conversationParams["their_relationship_to_me"]
    tone_of_chat = conversationParams["tone_of_chat"]
    previous_messages = conversationParams["previous_messages"]

    prompt = f"""
The following is a conversation between {my_name} and {their_name}, who is {my_name}'s {their_relationship_to_me}.  
{my_name} is a {my_age} year old {my_occupation} who lives in {my_location}.  {my_pronoun} likes to {my_hobbies}.  
{my_pronoun} can be described as {my_traits}.  The tone of this conversation is {tone_of_chat}.

"""

    for message in previous_messages:
        prompt += f"{message['author']}: {message['text']}\n"

    # Generate the next message from the perspective of me
    prompt += f"{my_name}:"

    return prompt


def map_completion_response_to_suggestions(response: GPT3CompletionResponse) -> list[Suggestion]:
    suggestions: list[Suggestion] = []

    for choice in response["choices"]:
        suggestion = choice["text"].lstrip()
        suggestions.append({"text": suggestion})

    return suggestions
