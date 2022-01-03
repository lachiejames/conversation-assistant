from typing_extensions import TypedDict

from conversation_assistant.models.message import Message

GPT3Params = TypedDict(
    "GPT3Params",
    {
        "randomness": float,
        "num_results": int,
        "max_length": int,
    },
)

LambdaEvent = TypedDict(
    "LambdaEvent",
    {
        "previous_messages": list[Message],
        "gpt3_params": GPT3Params,
    },
)
