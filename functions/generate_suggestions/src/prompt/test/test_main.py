from unittest.mock import MagicMock, patch

from ...test.mocks import EMPTY_REQUEST, EMPTY_REQUEST_WITH_NAMES
from ...utils import DEFAULT_LANG
from ..main import construct_prompt


def test_construct_prompt__when_all_params_given__then_return_everything() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Serious conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.

Stacey: Hey Chad!

Chad Johnson: What's crackin babydoll

Stacey: I think I'm pregnant...

Chad Johnson: Damn that's crazy

<Rephrase Chad Johnson's message so that it sounds more Serious>

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_all_params_except_names_given__then_omit_names() -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Serious conversation that I had with my Friend.
I am 27 years old.
My pronouns are he/him.
I live in Camberwell, Victoria, Australia.
My occupation is Software Engineer.
My hobbies include coding, hanging out with my dog.
People describe me as a cool guy who always knows the right thing to say.

Friend: Hey Chad!

Me: What's crackin babydoll

Friend: I think I'm pregnant...

Me: Damn that's crazy

<Rephrase my message so that it sounds more Serious>

Me:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_all_params_except_rephrase_given__then_omit_comment() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Casual"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Casual conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.

Stacey: Hey Chad!

Chad Johnson: What's crackin babydoll

Stacey: I think I'm pregnant...

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_all_params_except_messages_given__then_omit_messages() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Casual"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Sup Stace, what's crack-a-lackin?"

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Casual conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.

Chad Johnson: Sup Stace, what's crack-a-lackin?

<Rephrase Chad Johnson's message so that it sounds more Casual>

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_all_params_except_messages_and_rephrase_given__then_omit_messages_and_comment() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Casual"

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Casual conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_no_profile_params_given__then_omit_extras() -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Serious conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.

Stacey: Hey Chad!

Chad Johnson: What's crackin babydoll

Stacey: I think I'm pregnant...

Chad Johnson: Damn that's crazy

<Rephrase Chad Johnson's message so that it sounds more Serious>

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_no_profile_params_or_names_given__then_omit_extras_and_names() -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a Serious conversation that I had with my Friend.

Friend: Hey Chad!

Me: What's crackin babydoll

Friend: I think I'm pregnant...

Me: Damn that's crazy

<Rephrase my message so that it sounds more Serious>

Me:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_nothing_given__then_return_expected_string() -> None:
    request = EMPTY_REQUEST.copy()

    prompt = construct_prompt(request, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a conversation that I had.

Me:"""
    assert prompt == expected_prompt


@patch("src.prompt.main.translate_text")
def test_construct_prompt__when_all_params_given_and_lang_not_english__then_translate_intro_and_extra(
    translate_text_spy: MagicMock,
) -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"
    request["previous_messages"] = [
        {
            "text": "Hey Chad!",
            "is_my_message": False,
        },
        {
            "text": "What's crackin babydoll",
            "is_my_message": True,
        },
        {
            "text": "I think I'm pregnant...",
            "is_my_message": False,
        },
    ]

    alt_lang = "it"
    construct_prompt(request, input_lang=alt_lang)
    expected_translate_input = """The following is a Serious conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.
"""
    translate_text_spy.assert_called_once_with(expected_translate_input, alt_lang)


@patch("src.prompt.main.translate_text")
def test_construct_prompt__when_no_messages_given_and_lang_not_english__then_translate_intro_and_extra(
    translate_text_spy: MagicMock,
) -> None:
    request = EMPTY_REQUEST_WITH_NAMES.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"

    alt_lang = "it"
    construct_prompt(request, input_lang=alt_lang)
    expected_translate_input = """The following is a Serious conversation between Chad Johnson and Stacey, who is Chad Johnson's Friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.
"""
    translate_text_spy.assert_called_once_with(expected_translate_input, alt_lang)


@patch("src.prompt.main.translate_text")
def test_construct_prompt__when_no_messages_or_names_given_and_lang_not_english__then_translate_intro_and_extra(
    translate_text_spy: MagicMock,
) -> None:
    request = EMPTY_REQUEST.copy()
    request["settings"]["profile_params"]["age"] = "27"
    request["settings"]["profile_params"]["pronouns"] = "he/him"
    request["settings"]["profile_params"]["location"] = "Camberwell, Victoria, Australia"
    request["settings"]["profile_params"]["occupation"] = "Software Engineer"
    request["settings"]["profile_params"]["hobbies"] = "coding, hanging out with my dog"
    request["settings"]["profile_params"]["self_description"] = "a cool guy who always knows the right thing to say"
    request["settings"]["conversation_params"]["their_relationship_to_me"] = "Friend"
    request["settings"]["conversation_params"]["tone_of_chat"] = "Serious"
    request["settings"]["conversation_params"]["message_to_rephrase"] = "Damn that's crazy"

    alt_lang = "it"
    construct_prompt(request, input_lang=alt_lang)
    expected_translate_input = """The following is a Serious conversation that I had with my Friend.
I am 27 years old.
My pronouns are he/him.
I live in Camberwell, Victoria, Australia.
My occupation is Software Engineer.
My hobbies include coding, hanging out with my dog.
People describe me as a cool guy who always knows the right thing to say.
"""
    translate_text_spy.assert_called_once_with(expected_translate_input, alt_lang)


@patch("src.prompt.main.translate_text")
def test_construct_prompt__when_nothing_given__then_translate_intro_and_extra(
    translate_text_spy: MagicMock,
) -> None:
    request = EMPTY_REQUEST.copy()

    alt_lang = "it"
    construct_prompt(request, input_lang=alt_lang)
    expected_translate_input = """The following is a conversation that I had.
"""
    translate_text_spy.assert_called_once_with(expected_translate_input, alt_lang)
