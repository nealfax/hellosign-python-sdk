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
        response = request.get(url='https://www.hellosign.com/',
                               headers={'Custom-Header': 'Nothing'},
                               parameters={'param': 'Nothing'},
                               get_json=False)
        self.assertEquals(response.status_code, 200)
        response = request.get(url='https://github.com/timeline.json',
                               get_json=True)
        # print response
        self.assertEquals(isinstance(response, list), True)
        self.assertEquals(isinstance(response[0], dict), True)

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
                                    headers={'Custom-Header': 'Nothing'},
                                    filename=temp_filename)
        os.unlink(f.name)
        self.assertEquals(response, True)

        response = request.get_file(url='https://www.hellosign.com/',
                                    headers={'Custom-Header': 'Nothing'},
                                    filename='')
        self.assertEquals(response, False)
