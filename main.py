from conversation_assistant.generator import generate_message_suggestions


generate_message_suggestions(
    [
        {"text": "Hey, how are you today?", "author": "Lachie James"},
        {"text": "Not too bad mate, how are you?", "author": "Me"},
        {"text": "Yeah good mate.  What have you been up to lately?", "author": "Lachie James"},
    ]
)
