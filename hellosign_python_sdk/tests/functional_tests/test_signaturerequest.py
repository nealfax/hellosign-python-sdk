from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.resource.account import Account
from hellosign_python_sdk.utils.exception import InvalidEmail, EmptyPassword


class TestSignatureRequest(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_account(self):
        pass
