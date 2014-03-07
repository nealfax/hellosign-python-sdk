from http.request import HSRequest
from http.exception import HSException
from resource.account import Account
from resource.signature_request import SignatureRequest
from resource.reusable_form import ReusableForm
from resource.team import Team
from resource.unclaimed_draft import UnclaimedDraft


class HSClient(object):

    """docstring for HSClient"""
    ACCOUNT_CREATE_URL = 'https://api.hellosign.com/v3/account/create'
    ACCOUNT_INFO_URL = 'https://api.hellosign.com/v3/account'
    ACCOUNT_UPDATE_URL = 'https://api.hellosign.com/v3/account'

    SIGNATURE_REQUEST_INFO_URL = 'https://api.hellosign.com/v3/signature_request/'
    SIGNATURE_REQUEST_LIST_URL = 'https://api.hellosign.com/v3/signature_request/list'
    SIGNATURE_REQUEST_DOWNLOAD_PDF_URL = 'https://api.hellosign.com/v3/signature_request/files/'
    SIGNATURE_REQUEST_DOWNLOAD_FINAL_COPY_URL = 'https://api.hellosign.com/v3/signature_request/files/'
    SIGNATURE_REQUEST_CREATE_URL = 'https://api.hellosign.com/v3/signature_request/send'
    SIGNATURE_REQUEST_CREATE_WITH_RF_URL = 'https://api.hellosign.com/v3/signature_request/send_with_reusable_form'
    SIGNATURE_REQUEST_REMIND_URL = 'https://api.hellosign.com/v3/signature_request/remind/'
    SIGNATURE_REQUEST_CANCEL_URL = 'https://api.hellosign.com/v3/signature_request/cancel/'
    SIGNATURE_REQUEST_CREATE_EMBEDDED_URL = 'https://api.hellosign.com/v3/signature_request/create_embedded'
    SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_RF_URL = 'https://api.hellosign.com/v3/signature_request/create_embedded_with_reusable_form'

    EMBEDDED_OBJECT_GET_URL = 'https://api.hellosign.com/v3/embedded/sign_url/'

    UNCLAIMED_DRAFT_CREATE_URL = 'https://api.hellosign.com/v3/unclaimed_draft/create'

    REUSABLE_FORM_GET_URL = 'https://api.hellosign.com/v3/reusable_form/'
    REUSABLE_FORM_GET_LIST_URL = 'https://api.hellosign.com/v3/reusable_form/list'
    REUSABLE_FORM_ADD_USER_URL = 'https://api.hellosign.com/v3/reusable_form/add_user/'
    REUSABLE_FORM_REMOVE_USER_URL = 'https://api.hellosign.com/v3/reusable_form/remove_user/'

    TEAM_INFO_URL = 'https://api.hellosign.com/v3/team'
    TEAM_CREATE_URL = 'https://api.hellosign.com/v3/team/create'
    TEAM_UPDATE_URL = 'https://api.hellosign.com/v3/team'
    TEAM_DESTROY_URL = 'https://api.hellosign.com/v3/team/destroy'
    TEAM_ADD_MEMBER_URL = 'https://api.hellosign.com/v3/team/add_member'
    TEAM_REMOVE_MEMBER_URL = 'https://api.hellosign.com/v3/team/remove_member'

    # TODO: Put api account in HSClient's __init__ function instead of
    # HSRequest

    def __init__(self):
        super(HSClient, self).__init__()
        self.account = Account()
        self.get_account_info()

    def create_account(self, email, password):
        # TODO: make the check exceptions
        if email is None:
            print("Email is not valid")
        if password is None:
            print("Password is not valid")
        request = HSRequest()
        response = request.post(self.ACCOUNT_CREATE_URL, {
                                'email_address': email, 'password': password})
        # print response
        return Account(response["account"])

    # Get account info and put in self.account
    def get_account_info(self):
        request = HSRequest()
        response = request.get(self.ACCOUNT_INFO_URL)
        # self.account = Account(response, "account")
        self.account.json_data = response["account"]

    def update_account_info(self):
        request = HSRequest()
        request.post(self.ACCOUNT_UPDATE_URL, {
                     'callback_url': self.account.callback_url})
        # return response

    # Get a signature request
    # param @signature_request_id
    def get_signature_request(self, signature_request_id):
        request = HSRequest()
        response = request.get(
            self.SIGNATURE_REQUEST_INFO_URL + signature_request_id)
        return SignatureRequest(response["signature_request"])

    def get_signature_request_list(self):
        sr_list = []
        request = HSRequest()
        response = request.get(self.SIGNATURE_REQUEST_LIST_URL)
        for signature_request in response["signature_requests"]:
            sr_list.append(SignatureRequest(signature_request))
        return sr_list

    def get_signature_request_file(self, signature_request_id, filename):
        request = HSRequest()
        request.get_file(
            self.SIGNATURE_REQUEST_DOWNLOAD_PDF_URL + signature_request_id, filename)

    def get_signature_request_final_copy(self, signature_request_id, filename):
        request = HSRequest()
        request.get_file(
            self.SIGNATURE_REQUEST_DOWNLOAD_FINAL_COPY_URL + signature_request_id, filename)

    # Use files instead of file to avoid python keyword
    # TODO: check and raise exceptions when required fields are empty
    def send_signature_request(self, test_mode=0, files=None, title=None,
                               subject=None, message=None,
                               signing_redirect_url=None, signers=None,
                               cc_email_addresses=None,
                               form_fields_per_document=None):
        files_payload = {}
        for idx, filename in enumerate(files):
            files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')
        # print files_payload
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
            "test_mode": test_mode, "title": title, "subject": subject, "message": message,
            "signing_redirect_url": signing_redirect_url, "form_fields_per_document": form_fields_per_document}
        # removed attributes with none value
        payload = dict((key, value)
                       for key, value in payload.iteritems() if value)

        request = HSRequest()
        response = request.post(
            self.SIGNATURE_REQUEST_CREATE_URL, data=dict(payload.items() + signers_payload.items()
                                                         + cc_email_addresses_payload.items()), files=files_payload)
        return SignatureRequest(response["signature_request"])

    # TODO: check and raise exceptions when required fields are empty
    def send_signature_request_with_rf(self, test_mode="0", reusable_form_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        signers_payload = {}
        for signer in signers:
            # print signer
            # signer: {"rolename": "Role Name", "name": "Name", "email_address": "email@email.email"}
            signers_payload["signers[" + signer["role_name"] + "][name]"] = signer["name"]
            signers_payload["signers[" + signer["role_name"] + "][email_address]"] = signer[
                "email_address"]
            if "pin" in signer:
                signers_payload[
                    "signers[" + signer["role_name"] + "][pin]"] = signer["pin"]

        ccs_payload = {}
        for cc in ccs:
            # cc_emaiL_address: {"email_address": "email@email.email", "role_name": "Role Name"}
            ccs_payload[
                "ccs[" + cc["role_name"] + "]"] = cc["email_address"]
        custom_fields_payload = {}
        # custom_field: {"name": value}
        for custom_field in custom_fields:
            for key, value in custom_field.iteritems():
                custom_fields_payload["custom_fields[" + key + "]"] = value

        payload = {
            "test_mode": test_mode, "reusable_form_id": reusable_form_id, "title": title, "subject": subject, "message": message,
            "signing_redirect_url": signing_redirect_url}
        # removed attributes with none value
        # TODO: make this a function to follow DRY principle
        payload = dict((key, value)
                       for key, value in payload.iteritems() if value)
        request = HSRequest()
        response = request.post(self.SIGNATURE_REQUEST_CREATE_WITH_RF_URL, data=dict(payload.items() + signers_payload.items() + ccs_payload.items() + custom_fields_payload.items()))
        return SignatureRequest(response["signature_request"])

    def remind_signature_request(self, signature_request_id, email_address):
        request = HSRequest()
        response = request.post(self.SIGNATURE_REQUEST_REMIND_URL + signature_request_id, data={"email_address": email_address})
        return SignatureRequest(response["signature_request"])

    # TODO: return True or False
    def cancel_signature_request(self, signature_request_id):
        request = HSRequest()
        response = request.post(self.SIGNATURE_REQUEST_CANCEL_URL + signature_request_id)
        return True

    # TODO: refactor the code to use the same logic with send_signature_request()
    def send_signature_request_embedded(self, test_mode="0", client_id=None, files=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, cc_email_addresses=None, form_fields_per_document=None):

        files_payload = {}
        for idx, filename in enumerate(files):
            # print filename
            files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')
        # print files_payload
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

        request = HSRequest()
        response = request.post(self.SIGNATURE_REQUEST_CREATE_EMBEDDED_URL, data=dict(payload.items() + signers_payload.items()
                                                         + cc_email_addresses_payload.items()), files=files_payload)
        return SignatureRequest(response["signature_request"])

    def send_signature_request_embedded_with_rf(self, test_mode="0", client_id=None, reusable_form_id=None, title=None, subject=None, message=None, signing_redirect_url=None, signers=None, ccs=None, custom_fields=None):
        signers_payload = {}
        for signer in signers:
            # print signer
            # signer: {"rolename": "Role Name", "name": "Name", "email_address": "email@email.email"}
            signers_payload["signers[" + signer["role_name"] + "][name]"] = signer["name"]
            signers_payload["signers[" + signer["role_name"] + "][email_address]"] = signer[
                "email_address"]
            if "pin" in signer:
                signers_payload[
                    "signers[" + signer["role_name"] + "][pin]"] = signer["pin"]

        ccs_payload = {}
        for cc in ccs:
            # cc_emaiL_address: {"email_address": "email@email.email", "role_name": "Role Name"}
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
        # removed attributes with none value
        # TODO: make this a function to follow DRY principle
        payload = dict((key, value)
                       for key, value in payload.iteritems() if value)
        request = HSRequest()
        response = request.post(self.SIGNATURE_REQUEST_CREATE_WITH_RF_URL, data=dict(payload.items() + signers_payload.items() + ccs_payload.items() + custom_fields_payload.items()))
        return SignatureRequest(response["signature_request"])

    def get_reusable_form(self, reusable_form_id):
        request = HSRequest()
        response = request.get(self.REUSABLE_FORM_GET_URL + reusable_form_id)
        return ReusableForm(response["reusable_form"])

    # TODO: return the total results (in another function, variable...)

    def get_reusable_form_list(self, page=1):
        rf_list = []
        request = HSRequest()
        response = request.get(
            self.REUSABLE_FORM_GET_LIST_URL, parameters={"page": page})
        # print response
        for reusable_form in response["reusable_forms"]:
            rf_list.append(ReusableForm(reusable_form))
            # print reusable_form
        return rf_list

    # RECOMMEND: this api does not fail if the user has been added...
    def add_user_to_reusable_form(self, reusable_form_id, account_id=None, email_address=None):
        if (email_address is None and account_id is None):
            raise HSException("No email address or account_id specified")
        request = HSRequest()
        data = {}
        if account_id is not None:
            data = {"account_id": account_id}
        else:
            data = {"email_address": email_address}
        request = HSRequest()
        response = request.post(self.REUSABLE_FORM_ADD_USER_URL + reusable_form_id, data)
        return ReusableForm(response["reusable_form"])

    # TODO: consider merging add & remove into one function, or using some same code...
    def remove_user_from_reusable_form(self, reusable_form_id, account_id=None, email_address=None):
        if (email_address is None and account_id is None):
            raise HSException("No email address or account_id specified")
        request = HSRequest()
        data = {}
        if account_id is not None:
            data = {"account_id": account_id}
        else:
            data = {"email_address": email_address}
        request = HSRequest()
        response = request.post(self.REUSABLE_FORM_REMOVE_USER_URL + reusable_form_id, data)
        return ReusableForm(response["reusable_form"])

    def get_team_info(self):
        request = HSRequest()
        response = request.get(self.TEAM_INFO_URL)
        return Team(response["team"])

    def create_team(self, name):
        request = HSRequest()
        response = request.post(self.TEAM_CREATE_URL, {"name": name})
        return Team(response["team"])

    # TODO: consider moving this function to Team class, or return something else (true, false, etc...)
    # The api event create a new team if you do not belong to any team
    def update_team_name(self, name):
        request = HSRequest()
        response = request.post(self.TEAM_UPDATE_URL, {"name": name})
        return True

    # TODO: return True or False
    def destroy_team(self):
        request = HSRequest()
        request.post(self.TEAM_DESTROY_URL)
        return True

    # TODO: move this function to Team object (class)
    # TODO: return some int values for diffrent results: eg,: 1 success, 0: fail, -1: user has been added before... (or use exceptions for handling this later...)
    def add_team_member(self, email_address=None, account_id=None):
        if (email_address is None and account_id is None):
            raise HSException("No email address or account_id specified")
        request = HSRequest()
        data = {}
        if account_id is not None:
            data = {"account_id": account_id}
        else:
            data = {"email_address": email_address}
        response = request.post(self.TEAM_ADD_MEMBER_URL, data)
        print response

    # TODO: move this function to Team object (class)
    # TODO: DRY (add & remove member)
    def remove_team_member(self, email_address=None, account_id=None):
        if (email_address is None and account_id is None):
            raise HSException("No email address or account_id specified")
        request = HSRequest()
        data = {}
        if account_id is not None:
            data = {"account_id": account_id}
        else:
            data = {"email_address": email_address}
        response = request.post(self.TEAM_REMOVE_MEMBER_URL, data)
        print response

    def get_embeded_object(self, signature_id):
        request = HSRequest()
        response = request.get(self.EMBEDDED_OBJECT_GET_URL, signature_id)
        return Embeded(response["embedded"])

    # TODO: DRY
    # RECOMMEND: no title?
    def create_unclaimed_draft(self, test_mode="0", files=None, draft_type=None, subject=None, message=None, signers=None, cc_email_addresses=None, signing_redirect_url=None, form_fields_per_document=None):
        files_payload = {}
        for idx, filename in enumerate(files):
            # print filename
            files_payload["file[" + str(idx) + "]"] = open(filename, 'rb')
        # print files_payload
        signers_payload = {}
        for idx, signer in enumerate(signers):
            # print signer
            if draft_type == UnclaimedDraft.UNCLAIMED_DRAFT_REQUEST_SIGNATURE_TYPE:
                if "name" not in signer and "email_address" not in signer:
                    raise HSException("Signer's name and email are required")
                else:
                    signers_payload["signers[" + str(idx) + "][name]"] = signer["name"]
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

        request = HSRequest()
        response = request.post(self.UNCLAIMED_DRAFT_CREATE_URL, data=dict(payload.items() + signers_payload.items()
                                                         + cc_email_addresses_payload.items()), files=files_payload)
        return UnclaimedDraft(response["unclaimed_draft"])

