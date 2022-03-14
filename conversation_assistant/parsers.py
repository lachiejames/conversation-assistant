from .models import (
    GenerateMessageSuggestionsRequest,
    GPT3CompletionResponse,
    Suggestion,
)


def generate_prompt(request: GenerateMessageSuggestionsRequest) -> str:
    my_name = request["profile_params"]["name"]
    my_age = request["profile_params"]["age"]
    my_pronoun = request["profile_params"]["pronoun"]
    my_location = request["profile_params"]["location"]
    my_occupation = request["profile_params"]["occupation"]
    my_traits = request["profile_params"]["traits"]
    my_hobbies = request["profile_params"]["hobbies"]

    their_name = request["conversation_params"]["their_name"]
    their_relationship_to_me = request["conversation_params"]["their_relationship_to_me"]
    tone_of_chat = request["conversation_params"]["tone_of_chat"]
    previous_messages = request["conversation_params"]["previous_messages"]

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
