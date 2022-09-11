from ...test.mocks import (
    MOCK_REQUEST,
    MOCK_REQUEST_NO_MESSAGES,
    MOCK_REQUEST_NO_NAMES,
    MOCK_REQUEST_NO_NAMES_NO_MESSAGES,
    MOCK_REQUEST_NOTHING,
)
from ...utils import DEFAULT_LANG, UNDEFINED_LANG
from ..main import construct_prompt


def test_construct_prompt__when_names_and_mains_given__then_return_string_with_names() -> None:
    prompt = construct_prompt(MOCK_REQUEST, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a casual conversation between Chad Johnson and Stacey, who is Chad Johnson's friend.
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


def test_construct_prompt__when_names_and_no_mains_given__then_return_expected_string() -> None:
    prompt = construct_prompt(MOCK_REQUEST_NO_MESSAGES, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a casual conversation between Chad Johnson and Stacey, who is Chad Johnson's friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_no_names_and_mains_given__then_return_expected_string() -> None:
    prompt = construct_prompt(MOCK_REQUEST_NO_NAMES, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a casual conversation that I had with my friend.
I am 27 years old.
My pronouns are he/him.
I live in Camberwell, Victoria, Australia.
My occupation is Software Engineer.
My hobbies include coding, hanging out with my dog.
People describe me as a cool guy who always knows the right thing to say.

Them: Hey Chad!

Me: What's crackin babydoll

Them: I think I'm pregnant...

Me:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_no_names_and_no_mains_given__then_return_expected_string() -> None:
    prompt = construct_prompt(MOCK_REQUEST_NO_NAMES_NO_MESSAGES, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a casual conversation between Chad Johnson and Stacey, who is Chad Johnson's friend.
Chad Johnson is 27 years old.
Chad Johnson's pronouns are he/him.
Chad Johnson lives in Camberwell, Victoria, Australia.
Chad Johnson's occupation is Software Engineer.
Chad Johnson's hobbies include coding, hanging out with my dog.
People describe Chad Johnson as a cool guy who always knows the right thing to say.

Chad Johnson:"""
    assert prompt == expected_prompt


def test_construct_prompt__when_nothing_given__then_return_expected_string() -> None:
    prompt = construct_prompt(MOCK_REQUEST_NOTHING, input_lang=DEFAULT_LANG)
    expected_prompt = """The following is a conversation that I had.

Me:"""
    assert prompt == expected_prompt
