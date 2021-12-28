from conversation_assistant.models.message import Message
from conversation_assistant.models.suggestion import Suggestion

MOCK_SUGGESTIONS: list[Suggestion] = [
    {
        "text": "\nI am a web developer.",
    },
    {
        "text": "\nI am a stay-at-home mom.",
    },
    {
        "text": "\nI am a software engineer.",
    },
]

MOCK_MESSAGES: list[Message] = [
    {"text": "Hey, how are you today?", "author": "Lachie James"},
    {"text": "Not too bad mate, how are you?", "author": "Me"},
    {"text": "Yeah good mate.  What have you been up to lately?", "author": "Lachie James"},
]

MOCK_PROMPT = """
Lachie James - Hey, how are you today?,
Me - Hi I am good.  I am 45, how old are you?,
Lachie James - I am 30, what do you do for work?,
Me - 
"""
