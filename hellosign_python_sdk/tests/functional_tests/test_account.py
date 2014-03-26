from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.resource.account import Account
from hellosign_python_sdk.utils.exception import InvalidEmail, EmptyPassword


class TestAccount(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_account(self):
        account = self.client.get_account_info()
        self.assertEquals(account, True)
        self.assertEquals(isinstance(self.client.account, Account), True)

        new_client = HSClient(api_key='non valid api key')
        account = new_client.get_account_info()
        self.assertEquals(account, False)

        # We update nothing, but the api returns an Account object, so it is
        # considered successful
        account = self.client.update_account_info()
        self.assertEquals(account, True)

        self.client.account.callback_url = 'not valid url'
        account = self.client.update_account_info()
        self.assertEquals(account, False)

        try:
            account = self.client.create_account("not valid email@example.com",
                                                 "password")
        except InvalidEmail:
            pass
        try:
            account = self.client.create_account("", "")
        except InvalidEmail:
            pass
        except EmptyPassword:
            pass
