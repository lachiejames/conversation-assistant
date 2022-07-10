import unittest
import unittest.mock

from main import hello_name, hello_world


class TestHello(unittest.TestCase):
    def test_hello_world(self):
        req = unittest.mock.Mock()

        # Call tested function
        assert hello_world(req) == "Hello World!"

    def test_hello_name_no_name(self):
        req = unittest.mock.Mock(args={})

        # Call tested function
        assert hello_name(req) == "Hello World!"

    def test_hello_name_with_name(self):
        name = "test"
        req = unittest.mock.Mock(args={"name": name})

        # Call tested function
        assert hello_name(req) == "Hello {}!".format(name)
