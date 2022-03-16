from typing_extensions import TypedDict

from .conversation_params import ConversationParams
from .gpt3_params import GPT3Params
from .profile_params import ProfileParams

GenerateMessageSuggestionsRequest = TypedDict(
    "GenerateMessageSuggestionsRequest",
    {
        "conversation_params": ConversationParams,
        "profile_params": ProfileParams,
        "gpt3_params": GPT3Params,
    },
)


LambdaEvent = TypedDict(
    "LambdaEvent",
    {
        # Stringified version of GenerateMessageSuggestionsRequest since Lambda's don't like JSON payloads
        "body": str,
    },
)
