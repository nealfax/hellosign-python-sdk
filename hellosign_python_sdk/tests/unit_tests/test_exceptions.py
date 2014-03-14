from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.exception import *


class TestException(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_hsexception(self):
        error = HSException("Message")
        self.assertEqual(str(error), "Message")

    def test_no_auth_method(self):
        error = NoAuthMethod("No authentication information found")
        self.assertEquals(str(error), "No authentication information found")

    def test_http_error(self):
        error = BadRequest("Bad Request")
        self.assertEquals(str(error), "Bad Request")
