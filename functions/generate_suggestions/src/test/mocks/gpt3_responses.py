from typing import cast

from openai.types.chat import ChatCompletion, ChatCompletionMessage
from openai.types.chat.chat_completion import Choice
from openai.types.completion import CompletionUsage

from ...models import GPT3CompletionResponse

MOCK_GPT3_COMPLETION_RESPONSE: ChatCompletion = ChatCompletion(
    created=1716109693,
    id="chatcmpl-9QWoXxy9dbbY6BOl2BTyMASoGJVQt",
    model="gpt-4o-2024-05-13",
    object="chat.completion",
    usage=CompletionUsage(
        completion_tokens=7,
        prompt_tokens=135,
        total_tokens=142,
    ),
    choices=[
        Choice(
            finish_reason="stop",
            index=0,
            logprobs=None,
            message=ChatCompletionMessage(
                content="Hey! I'm Chad, 26 years old and a software developer. What about you?",
                role="assistant",
            ),
        ),
        Choice(
            finish_reason="stop",
            index=1,
            logprobs=None,
            message=ChatCompletionMessage(
                content="Hey there!",
                role="assistant",
            ),
        ),
        Choice(
            finish_reason="stop",
            index=2,
            logprobs=None,
            message=ChatCompletionMessage(
                content="From your profile it looks like we have a lot in common so I'd love to chat with you more if you're interested?",
                role="assistant",
            ),
        ),
    ],
)

MOCK_GPT3_COMPLETION_RESPONSE_DICT: GPT3CompletionResponse = cast(GPT3CompletionResponse, MOCK_GPT3_COMPLETION_RESPONSE.to_dict())


class MockMalformedResponse:
    def to_dict(self) -> dict[str, object]:
        return {"this": "will fail"}
