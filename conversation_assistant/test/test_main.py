import unittest
import unittest.mock
from conversation_assistant.test.mocks import MOCK_REQUEST, MOCK_SUGGESTIONS

from main import generate_suggestions


class TestHello(unittest.TestCase):
    def test_generate_suggestions_no_name(self):
        req = MOCK_REQUEST

        # Call tested function
        assert generate_suggestions(req) == MOCK_SUGGESTIONS

