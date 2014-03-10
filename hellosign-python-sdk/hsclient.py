from utils.request import HSRequest
from utils.exception import *
from resource.account import Account
from resource.signature_request import SignatureRequest
from resource.reusable_form import ReusableForm
from resource.team import Team
from resource.unclaimed_draft import UnclaimedDraft
import utils.utils as utils
from requests.auth import HTTPBasicAuth
from utils.hsaccesstokenauth import HSAccessTokenAuth


class HSClient(object):

    """docstring for HSClient"""
    API_VERSION = 'v3'
    API_URL = 'https://api.hellosign.com/' + API_VERSION

    ACCOUNT_CREATE_URL = API_URL + '/account/create'
    ACCOUNT_INFO_URL = API_URL + '/account'
    ACCOUNT_UPDATE_URL = API_URL + '/account'

    SIGNATURE_REQUEST_INFO_URL = API_URL + '/signature_request/'
    SIGNATURE_REQUEST_LIST_URL = API_URL + '/signature_request/list'
    SIGNATURE_REQUEST_DOWNLOAD_PDF_URL = API_URL + '/signature_request/files/'
    SIGNATURE_REQUEST_DOWNLOAD_FINAL_COPY_URL = API_URL + \
        '/signature_request/files/'
    SIGNATURE_REQUEST_CREATE_URL = API_URL + '/signature_request/send'
    SIGNATURE_REQUEST_CREATE_WITH_RF_URL = API_URL + \
        '/signature_request/send_with_reusable_form'
    SIGNATURE_REQUEST_REMIND_URL = API_URL + '/signature_request/remind/'
    SIGNATURE_REQUEST_CANCEL_URL = API_URL + '/signature_request/cancel/'
    SIGNATURE_REQUEST_CREATE_EMBEDDED_URL = API_URL + \
        '/signature_request/create_embedded'
    SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_RF_URL = API_URL + \
        '/signature_request/create_embedded_with_reusable_form'

    EMBEDDED_OBJECT_GET_URL = API_URL + '/embedded/sign_url/'

    UNCLAIMED_DRAFT_CREATE_URL = API_URL + '/unclaimed_draft/create'

    REUSABLE_FORM_GET_URL = API_URL + '/reusable_form/'
    REUSABLE_FORM_GET_LIST_URL = API_URL + '/reusable_form/list'
    REUSABLE_FORM_ADD_USER_URL = API_URL + '/reusable_form/add_user/'
    REUSABLE_FORM_REMOVE_USER_URL = API_URL + '/reusable_form/remove_user/'

    TEAM_INFO_URL = TEAM_UPDATE_URL = API_URL + '/team'
    TEAM_CREATE_URL = API_URL + '/team/create'
    TEAM_DESTROY_URL = API_URL + '/team/destroy'
    TEAM_ADD_MEMBER_URL = API_URL + '/team/add_member'
    TEAM_REMOVE_MEMBER_URL = API_URL + '/team/remove_member'

    # TODO: Put api account in HSClient's __init__ function instead of
    # HSRequest

    def __init__(self, api_email=None, api_password=None, api_key=None, api_accesstoken=None, api_accesstokentype=None):
        super(HSClient, self).__init__()
        self.auth = self._authenticate(
            api_email, api_password, api_key, api_accesstoken, api_accesstokentype)
        self.account = Account()
        # self.get_account_info()

    def create_account(self, email, password):
        if email is None:
            raise InvalidEmail("Email cannot be empty")
        elif not utils.is_email(email):
            raise InvalidEmail("Email is not valid")
        if password is None:
            raise EmptyPassword("Password cannot be empty")
        request = HSRequest(self.auth)
        response = request.post(self.ACCOUNT_CREATE_URL, {
                                'email_address': email, 'password': password})
        return Account(response["account"])

    # Get account info and put in self.account so that further access to the
    # info can be made by using self.account.attribute
    def get_account_info(self):
        request = HSRequest(self.auth)
        try:
            response = request.get(self.ACCOUNT_INFO_URL)
            self.account.json_data = response["account"]
        except HTTPError:
            return False
        return True

    # At the moment you can only update your callback_url only
    def update_account_info(self):
        request = HSRequest(self.auth)
        try:
            response = request.post(self.ACCOUNT_UPDATE_URL, {
                'callback_url': self.account.callback_url})
        except HTTPError:
            return False
        return True

    # Get a signature request
    # param @signature_request_id
    def get_signature_request(self, signature_request_id):
        request = HSRequest(self.auth)
        response = request.get(
            self.SIGNATURE_REQUEST_INFO_URL + signature_request_id)
        return SignatureRequest(response["signature_request"])

    def get_signature_request_list(self):
        sr_list = []
        request = HSRequest(self.auth)
        response = request.get(self.SIGNATURE_REQUEST_LIST_URL)
        for signature_request in response["signature_requests"]:
            sr_list.append(SignatureRequest(signature_request))
        return sr_list

    def get_signature_request_file(self, signature_request_id, filename):
        request = HSRequest(self.auth)
        request.get_file(
            self.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL + signature_request_id, filename)

    def get_signature_request_final_copy(self, signature_request_id, filename):
        # This api call is DEPRECATED
        request = HSRequest(self.auth)
        request.get_file(
            self.SIGNATURE_REQUEST_DOWNLOAD_FINAL_COPY_URL + signature_request_id, filename)

    # Use files instead of file to avoid python keyword
    def send_signature_request(
        self, test_mode="0", files=None, file_urls=None, title=None,
        subject=None, message=None,
        signing_redirect_url=None, signers=None,
        cc_email_addresses=None,
        form_fields_per_document=None):

        self._check_required_fields(
            {"signers": signers}, [{"files": files, "file_urls": file_urls}])
        return self._send_signature_request(test_mode=test_mode, files=files, file_urls=file_urls, title=title, subject=subject, message=message, signing_redirect_url=signing_redirect_url, signers=signers, cc_email_addresses=cc_email_addresses, form_fields_per_document=form_fields_per_document)

    # TODO: check and raise exceptions when required fields are empty
    def send_signature_request_with_rf(self, test_mode="0", reusable_form_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        self._check_required_fields(
            {"signers": signers, "reusable_form_id": reusable_form_id})
        return self._send_signature_request_with_rf(test_mode=test_mode, reusable_form_id=reusable_form_id, title=title, subject=subject, message=message, signing_redirect_url=signing_redirect_url, signers=signers, ccs=ccs, custom_fields=custom_fields)

    def remind_signature_request(self, signature_request_id, email_address):
        request = HSRequest(self.auth)
        response = request.post(self.SIGNATURE_REQUEST_REMIND_URL +
                                signature_request_id, data={"email_address": email_address})
        return SignatureRequest(response["signature_request"])

    def cancel_signature_request(self, signature_request_id):
        request = HSRequest(self.auth)
        try:
            response = request.post(
                self.SIGNATURE_REQUEST_CANCEL_URL + signature_request_id)
        except HTTPError:
            return False
        return True

    def send_signature_request_embedded(self, test_mode="0", client_id=None, files=None, file_urls=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, cc_email_addresses=None, form_fields_per_document=None):

        self._check_required_fields(
            {"signers": signers, "client_id": client_id}, [{"files": files, "file_urls": file_urls}])
        return self._send_signature_request(test_mode=test_mode, client_id=client_id, files=files, file_urls=file_urls, title=title, subject=subject, message=message, signing_redirect_url=signing_redirect_url, signers=signers, cc_email_addresses=cc_email_addresses, form_fields_per_document=form_fields_per_document)

    def send_signature_request_embedded_with_rf(self, test_mode="0", client_id=None, reusable_form_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        self._check_required_fields(
            {"signers": signers, "reusable_form_id": reusable_form_id, "client_id": client_id})
        return self._send_signature_request_with_rf(test_mode=test_mode, client_id=client_id, reusable_form_id=reusable_form_id, title=title, subject=subject, message=message, signing_redirect_url=signing_redirect_url, signers=signers, ccs=ccs, custom_fields=custom_fields)

    def get_reusable_form(self, reusable_form_id):
        request = HSRequest(self.auth)
        response = request.get(self.REUSABLE_FORM_GET_URL + reusable_form_id)
        return ReusableForm(response["reusable_form"])

    # TODO: return the total results (in another function, variable...)
    def get_reusable_form_list(self, page=1):
        rf_list = []
        request = HSRequest(self.auth)
        response = request.get(
            self.REUSABLE_FORM_GET_LIST_URL, parameters={"page": page})
        # print response
        for reusable_form in response["reusable_forms"]:
            rf_list.append(ReusableForm(reusable_form))
            # print reusable_form
        return rf_list

    # RECOMMEND: this api does not fail if the user has been added...
    def add_user_to_reusable_form(self, reusable_form_id, account_id=None, email_address=None):
        return self._add_remove_user_reusable_form(self.REUSABLE_FORM_ADD_USER_URL, reusable_form_id, account_id, email_address)

    def remove_user_from_reusable_form(self, reusable_form_id, account_id=None, email_address=None):
        return self._add_remove_user_reusable_form(self.REUSABLE_FORM_REMOVE_USER_URL, reusable_form_id, account_id, email_address)

    def get_team_info(self):
        request = HSRequest(self.auth)
        response = request.get(self.TEAM_INFO_URL)
        return Team(response["team"])

    def create_team(self, name):
        request = HSRequest(self.auth)
        response = request.post(self.TEAM_CREATE_URL, {"name": name})
        return Team(response["team"])

    # The api event create a new team if you do not belong to any team
    def update_team_name(self, name):
        request = HSRequest(self.auth)
        try:
            response = request.post(self.TEAM_UPDATE_URL, {"name": name})
        except HTTPError:
            return False
        return True

    def destroy_team(self):
        request = HSRequest(self.auth)
        try:
            request.post(self.TEAM_DESTROY_URL)
        except HTTPError:
            return False
        return True

    def add_team_member(self, email_address=None, account_id=None):
        return self._add_remove_team_member(self.TEAM_ADD_MEMBER_URL, email_address, account_id)

    # RECOMMEND: does not fail if user has been removed
    def remove_team_member(self, email_address=None, account_id=None):
        return self._add_remove_team_member(self.TEAM_REMOVE_MEMBER_URL, email_address, account_id)

    def get_embeded_object(self, signature_id):
        request = HSRequest(self.auth)
        response = request.get(self.EMBEDDED_OBJECT_GET_URL, signature_id)
        return Embeded(response["embedded"])

    # RECOMMEND: no title?
    def create_unclaimed_draft(self, test_mode="0", files=None, file_urls=None, draft_type=None, subject=None, message=None, signers=None, cc_email_addresses=None, signing_redirect_url=None, form_fields_per_document=None):
        files_payload = {}
        for idx, filename in enumerate(files):
            files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')
        file_urls_payload = {}
        for idx, fileurl in enumerate(file_urls):
            file_urls_payload["file_url[" + str(idx) + "]"] = fileurl
        signers_payload = {}
        for idx, signer in enumerate(signers):
            # print signer
            if draft_type == UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE:
                if "name" not in signer and "email_address" not in signer:
                    raise HSException("Signer's name and email are required")
                else:
                    signers_payload[
                        "signers[" + str(idx) + "][name]"] = signer["name"]
                    signers_payload["signers[" + str(idx) + "][email_address]"] = signer[
                        "email_address"]
            if "order" in signer:
                signers_payload[
                    "signers[" + str(idx) + "][order]"] = signer["order"]
        cc_email_addresses_payload = {}
        for idx, cc_email_address in enumerate(cc_email_addresses):
            cc_email_addresses_payload[
                "cc_email_addresses[" + str(idx) + "]"] = cc_email_address
        payload = {
            "test_mode": test_mode, "type": draft_type, "subject": subject, "message": message,
            "signing_redirect_url": signing_redirect_url, "form_fields_per_document": form_fields_per_document}
        # removed attributes with none value
        payload = dict((key, value)
                       for key, value in payload.iteritems() if value)

        request = HSRequest(self.auth)
        response = request.post(self.UNCLAIMED_DRAFT_CREATE_URL, data=dict(payload.items() + signers_payload.items()
                                                                           + cc_email_addresses_payload.items() + file_urls_payload.items()), files=files_payload)
        return UnclaimedDraft(response["unclaimed_draft"])

    def _authenticate(self, api_email=None, api_password=None, api_key=None, api_accesstoken=None, api_accesstokentype=None):
        if api_accesstokentype and api_accesstoken:
            return HSAccessTokenAuth(api_accesstokentype, api_accesstoken)
        elif api_key:
            return HTTPBasicAuth(api_key, '')
        elif api_email and api_password:
            return HTTPBasicAuth(api_email, api_password)
        else:
            raise NoAuthMethod("No authentication information found!")

    def _check_required_fields(self, fields={}, either_fields=None):
        for key, value in fields.iteritems():
            # If value is a dict, one of the fields in the dict is required -> exception if all are None
            # if type(value) is 'dict':
            #     if not any(someDict.values()):
            if not value:
                raise HSException("Field " + key + " is required.")
        if either_fields is not None:
            print either_fields
            for field in either_fields:
                if not any(field.values()):
                    raise HSException(
                        "One of the fields in " + ", ".join(field.keys()) + " is required.")

    # To share the same logic between send_signature_request &
    # send_signature_request_embedded
    def _send_signature_request(self, test_mode="0", client_id=None, files=None, file_urls=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, cc_email_addresses=None, form_fields_per_document=None):
        files_payload = {}
        for idx, filename in enumerate(files):
            # print filename
            files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')
        # print files_payload
        file_urls_payload = {}
        for idx, fileurl in enumerate(file_urls):
            file_urls_payload["file_url[" + str(idx) + "]"] = fileurl
        signers_payload = {}
        for idx, signer in enumerate(signers):
            # print signer
            signers_payload["signers[" + str(idx) + "][name]"] = signer["name"]
            signers_payload["signers[" + str(idx) + "][email_address]"] = signer[
                "email_address"]
            if "order" in signer:
                signers_payload[
                    "signers[" + str(idx) + "][order]"] = signer["order"]
            if "pin" in signer:
                signers_payload[
                    "signers[" + str(idx) + "][pin]"] = signer["pin"]
        cc_email_addresses_payload = {}
        for idx, cc_email_address in enumerate(cc_email_addresses):
            cc_email_addresses_payload[
                "cc_email_addresses[" + str(idx) + "]"] = cc_email_address
        payload = {
            "test_mode": test_mode, "client_id": client_id, "title": title, "subject": subject, "message": message,
            "signing_redirect_url": signing_redirect_url, "form_fields_per_document": form_fields_per_document}
        # removed attributes with none value
        payload = dict((key, value)
                       for key, value in payload.iteritems() if value)

        request = HSRequest(self.auth)
        url = self.SIGNATURE_REQUEST_CREATE_URL
        if client_id:
            url = self.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL
        response = request.post(url, data=dict(payload.items() + signers_payload.items()
                                               + cc_email_addresses_payload.items() + file_urls_payload.items()), files=files_payload)
        return SignatureRequest(response["signature_request"])

    # To share the same logic between send_signature_request_with_rf and send_signature_request_embedded_with_rf
    def _send_signature_request_with_rf(self, test_mode="0", client_id=None, reusable_form_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        signers_payload = {}
        for signer in signers:
            signers_payload[
                "signers[" + signer["role_name"] + "][name]"] = signer["name"]
            signers_payload["signers[" + signer["role_name"] + "][email_address]"] = signer[
                "email_address"]
            if "pin" in signer:
                signers_payload[
                    "signers[" + signer["role_name"] + "][pin]"] = signer["pin"]

        ccs_payload = {}
        for cc in ccs:
            # cc_emaiL_address: {"email_address": "email@email.email",
            # "role_name": "Role Name"}
            ccs_payload[
                "ccs[" + cc["role_name"] + "]"] = cc["email_address"]
        custom_fields_payload = {}
        # custom_field: {"name": value}
        for custom_field in custom_fields:
            for key, value in custom_field.iteritems():
                custom_fields_payload["custom_fields[" + key + "]"] = value

        payload = {
            "test_mode": test_mode, "client_id": client_id, "reusable_form_id": reusable_form_id, "title": title, "subject": subject, "message": message,
            "signing_redirect_url": signing_redirect_url}
        # removed attributes with empty value
        payload = dict((key, value)
                       for key, value in payload.iteritems() if value)
        request = HSRequest(self.auth)
        url = self.SIGNATURE_REQUEST_CREATE_WITH_RF_URL
        if client_id:
            url = self.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_RF_URL
        response = request.post(url, data=dict(
            payload.items() + signers_payload.items() + ccs_payload.items() + custom_fields_payload.items()))
        return SignatureRequest(response["signature_request"])


    def _add_remove_user_reusable_form(self, url, reusable_form_id, account_id=None, email_address=None):
        if (email_address is None and account_id is None):
            raise HSException("No email address or account_id specified")
        request = HSRequest(self.auth)
        data = {}
        if account_id is not None:
            data = {"account_id": account_id}
        else:
            data = {"email_address": email_address}
        request = HSRequest(self.auth)
        response = request.post(url + reusable_form_id, data)
        return ReusableForm(response["reusable_form"])

    def _add_remove_team_member(self, url, email_address=None, account_id=None):
        if (email_address is None and account_id is None):
            raise HSException("No email address or account_id specified")
        request = HSRequest(self.auth)
        data = {}
        if account_id is not None:
            data = {"account_id": account_id}
        else:
            data = {"email_address": email_address}
        try:
            print request.post(url, data)
        except HTTPError:
            return False
        return True
