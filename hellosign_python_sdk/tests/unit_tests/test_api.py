from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.request import HSRequest


class Api(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_endpoint(self):
        self.assertEqual(HSClient.API_URL, "https://api.hellosign.com/v3")
        # account info, ...

    def test_get(self):
        request = HSRequest(self.client.auth)
        response = request.get(url='https://www.hellosign.com/', get_json=False)
        self.assertEquals(response.status_code, 200)

    # def test_post(self):
    #     self.api.request.return_value = {'id': 'test'}
    #     credit_card = self.api.post("v1/vault/credit-card", self.card_attributes)


    #     self.assertEqual(credit_card.get('error'), None)
    #     self.assertNotEqual(credit_card.get('id'), None)

    # def test_bad_request(self):
    #     self.api.request.return_value = {'error': 'test'}
    #     credit_card = self.api.post("v1/vault/credit-card", {})

    #     self.api.request.assert_called_once_with('https://api.sandbox.paypal.com/v1/vault/credit-card',
    #         'POST',
    #         body='{}',
    #         headers={})
    #     self.assertNotEqual(credit_card.get('error'), None)

    # def test_expired_time(self):
    #     old_token = self.api.get_token()
    #     self.api.token_hash["expires_in"] = 0
    #     self.assertNotEqual(self.api.get_token(), old_token)

    # def test_not_found(self):
    #     self.api.request.side_effect = paypal.ResourceNotFound("error")
    #     self.assertRaises(paypal.ResourceNotFound, self.api.get, ("/v1/payments/payment/PAY-1234"))