from conversation_assistant.validate_schema import validate_message_suggestions


def test_validate_message_suggestions():
    validate_message_suggestions(
        {
            "body": {
                "previous_messages": [],
                "gpt3_params": {
                    "randomness": 0.7,
                    "num_results": 3,
                    "max_length": 50,
                },
            }
        }
    )
