from unittest import TestCase
from hellosign_python_sdk.tests.test_helper import api_key
from hellosign_python_sdk.hsclient import HSClient
from hellosign_python_sdk.utils.request import HSRequest
from hellosign_python_sdk.utils.exception import BadRequest, NotFound, Unauthorized
from requests.auth import HTTPBasicAuth


class Api(TestCase):

    def setUp(self):
        self.client = HSClient(api_key=api_key)

    def test_endpoint(self):
        self.assertEqual(HSClient.API_URL,
                         "https://api.hellosign.com/v3")
        self.assertEqual(HSClient.ACCOUNT_CREATE_URL,
                         "https://api.hellosign.com/v3/account/create")
        self.assertEqual(HSClient.ACCOUNT_INFO_URL,
                         "https://api.hellosign.com/v3/account")
        self.assertEqual(HSClient.ACCOUNT_UPDATE_URL,
                         "https://api.hellosign.com/v3/account")

        self.assertEqual(HSClient.SIGNATURE_REQUEST_INFO_URL,
                         "https://api.hellosign.com/v3/signature_request/")
        self.assertEqual(HSClient.SIGNATURE_REQUEST_LIST_URL,
                         "https://api.hellosign.com/v3/signature_request/list")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL,
            "https://api.hellosign.com/v3/signature_request/files/")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_DOWNLOAD_FINAL_COPY_URL,
            "https://api.hellosign.com/v3/signature_request/files/")
        self.assertEqual(HSClient.SIGNATURE_REQUEST_CREATE_URL,
                         "https://api.hellosign.com/v3/signature_request/send")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_CREATE_WITH_RF_URL,
            "https://api.hellosign.com/v3/signature_request/" +
            "send_with_reusable_form")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_REMIND_URL,
            "https://api.hellosign.com/v3/signature_request/remind/")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_CANCEL_URL,
            "https://api.hellosign.com/v3/signature_request/cancel/")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL,
            "https://api.hellosign.com/v3/signature_request/create_embedded")
        self.assertEqual(
            HSClient.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_RF_URL,
            "https://api.hellosign.com/v3/signature_request/" +
            "create_embedded_with_reusable_form")

        self.assertEqual(HSClient.EMBEDDED_OBJECT_GET_URL,
                         "https://api.hellosign.com/v3/embedded/sign_url/")

        self.assertEqual(HSClient.UNCLAIMED_DRAFT_CREATE_URL,
                         "https://api.hellosign.com/v3/unclaimed_draft/create")

        self.assertEqual(HSClient.REUSABLE_FORM_GET_URL,
                         "https://api.hellosign.com/v3/reusable_form/")
        self.assertEqual(HSClient.REUSABLE_FORM_GET_LIST_URL,
                         "https://api.hellosign.com/v3/reusable_form/list")
        self.assertEqual(HSClient.REUSABLE_FORM_ADD_USER_URL,
                         "https://api.hellosign.com/v3/reusable_form/add_user/")
        self.assertEqual(
            HSClient.REUSABLE_FORM_REMOVE_USER_URL,
            "https://api.hellosign.com/v3/reusable_form/remove_user/")

        self.assertEqual(HSClient.TEAM_INFO_URL,
                         "https://api.hellosign.com/v3/team")
        self.assertEqual(HSClient.TEAM_CREATE_URL,
                         "https://api.hellosign.com/v3/team/create")
        self.assertEqual(HSClient.TEAM_UPDATE_URL,
                         "https://api.hellosign.com/v3/team")
        self.assertEqual(HSClient.TEAM_DESTROY_URL,
                         "https://api.hellosign.com/v3/team/destroy")
        self.assertEqual(HSClient.TEAM_ADD_MEMBER_URL,
                         "https://api.hellosign.com/v3/team/add_member")
        self.assertEqual(HSClient.TEAM_REMOVE_MEMBER_URL,
                         "https://api.hellosign.com/v3/team/remove_member")

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

    def test_not_authorized(self):
        request = HSRequest(HTTPBasicAuth("test", ''))
        try:
            request.get(HSClient.ACCOUNT_INFO_URL)
        except Unauthorized:
            pass

    def test_not_found(self):
        request = HSRequest(self.client.auth)
        try:
            request.get(url=HSClient.API_URL + "/not/found")
        except NotFound:
            pass
