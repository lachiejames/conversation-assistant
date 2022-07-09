from typing import TypedDict

GPT3Params = TypedDict(
    "GPT3Params",
    {
        "engine": str,
        "n": int,
        "temperature": float,
        "max_tokens": int,
        "top_p": float,
        "best_of": int,
        "frequency_penalty": float,
        "presence_penalty": float,
        "stop": list[str],
    },
)
