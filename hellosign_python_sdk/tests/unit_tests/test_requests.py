from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.request import HSRequest
import tempfile
import os


class Api(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_get(self):
        request = HSRequest(self.client.auth)
        response = request.get(url='https://www.hellosign.com/', get_json=False)
        self.assertEquals(response.status_code, 200)

    def test_post(self):
        request = HSRequest(self.client.auth)
        response = request.post(url='https://www.hellosign.com/',
                                data={"test": "None"}, get_json=False)
        self.assertEquals(response.status_code, 200)

    def test_get_file(self):
        request = HSRequest(self.client.auth)
        f = tempfile.NamedTemporaryFile(delete=True)
        temp_filename = f.name
        f.close()
        response = request.get_file(url='https://www.hellosign.com/',
                                    filename=temp_filename)
        os.unlink(f.name)
        self.assertEquals(response, True)
