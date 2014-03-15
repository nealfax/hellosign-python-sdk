from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.exception import *
from hellosign_python_sdk.resource.account import Account
from hellosign_python_sdk.resource.embedded import Embedded


class TestException(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_account(self):
        account = Account({'account_id': '123456790', 'is_paid_hf': False,
                          'quotas': {'documents_left': 3, 'templates_left': 0,
                          'api_signature_requests_left': 0},
                          'role_code': 'a', 'is_paid_hs': False, 'callback_url':
                          'http://www.example.com/callback',
                          'email_address': 'user@example.com'})
        self.assertEquals(account.account_id, '123456790')
        self.assertEquals(account.is_paid_hf, False)
        self.assertEquals(account.quotas['documents_left'], 3)
        self.assertEquals(account.quotas['templates_left'], 0)
        self.assertEquals(account.quotas['api_signature_requests_left'], 0)
        self.assertEquals(account.role_code, 'a')
        self.assertEquals(account.is_paid_hs, False)
        self.assertEquals(account.callback_url,
                          'http://www.example.com/callback')
        self.assertEquals(account.email_address, 'user@example.com')

    def test_embedded(self):
        embedded = Embedded({'sign_url': 'https://example.com/test/',
                            'expires_at': 1394859405})
        self.assertEquals(embedded.sign_url, 'https://example.com/test/')
        self.assertEquals(embedded.expires_at, 1394859405)
