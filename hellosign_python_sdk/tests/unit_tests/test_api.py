from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.request import HSRequest
from hellosign_python_sdk.utils.exception import BadRequest, NotFound


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

    def test_post(self):
        request = HSRequest(self.client.auth)
        response = request.post(url='https://www.hellosign.com/',
                                data={"test": "None"}, get_json=False)
        self.assertEquals(response.status_code, 200)

    def test_bad_request(self):
        request = HSRequest(self.client.auth)
        try:
            request.post(url=HSClient.ACCOUNT_UPDATE_URL,
                         data={"bad": "request"})
        except BadRequest:
            pass

    def test_not_found(self):
        request = HSRequest(self.client.auth)
        try:
            request.get(url=HSClient.API_URL + "/not/found")
        except NotFound:
            pass
