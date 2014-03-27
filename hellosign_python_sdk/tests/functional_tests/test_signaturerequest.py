from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.resource.signature_request import SignatureRequest
from hellosign_python_sdk.utils.exception import Forbidden
import tempfile


class TestSignatureRequest(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_signature_request(self):
        srl = self.client.get_signature_request_list()
        self.assertTrue(isinstance(srl, list))
        if len(srl) > 0:
            self.assertTrue(isinstance(srl[0], SignatureRequest))
            sr = self.client.get_signature_request(srl[0].signature_request_id)
            self.assertTrue(isinstance(sr, SignatureRequest))
            # Remind
            signer = srl[0].signatures[0]['signer_email_address']
            try:
                new_sr = self.client.remind_signature_request(srl[0].signature_request_id, signer)
                self.assertEquals(isinstance(new_sr, SignatureRequest), True)
            except Forbidden:
                pass
            # Download
            f = tempfile.NamedTemporaryFile(delete=True)
            temp_filename = f.name
            f.close()
            result = self.client.get_signature_request_file(srl[0].signature_request_id, temp_filename)
            self.assertTrue(result)

            result = self.client.get_signature_request_final_copy(srl[0].signature_request_id, temp_filename)
            self.assertTrue(result)
