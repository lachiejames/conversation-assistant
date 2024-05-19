from typing import List, Optional, TypedDict


class Message(TypedDict):
    content: str
    role: str


class GPT3CompletionChoices(TypedDict):
    finish_reason: str
    index: int
    logprobs: Optional[None]  # Assuming logprobs can be None
    message: Message


class GPT3Usage(TypedDict):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class GPT3CompletionResponse(TypedDict):
    choices: List[GPT3CompletionChoices]
    created: int
    id: str
    model: str
    object: str
    system_fingerprint: str
    usage: GPT3Usage
