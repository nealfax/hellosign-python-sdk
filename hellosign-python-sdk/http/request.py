import os
import requests
from requests.auth import HTTPBasicAuth
from exception import *
from hsaccesstokenauth import HSAccessTokenAuth


class HSRequest(object):

    DEFAULT_ENCODING = "UTF-8"
    USER_AGENT = "HelloSign Java SDK"
    url = ""
    parameters = {}
    headers = {'User-Agent': USER_AGENT}
    auth = None

    API_EMAIL = "minhdanh@siliconstraits.vn"
    API_PASSWORD = "miCSnwVp2qkZa73WjE"
    # API_EMAIL = ""
    # API_PASSWORD = ""
    API_KEY = ""
    API_ACCESSTOKEN = ""
    API_ACCESSTOKENTYPE = ""

    def __init__(self):
        self.auth = self._authenticate()

    def get(self, url, headers={}, parameters={}):
        response = requests.get(
            url, headers=dict(self.headers.items() + headers.items()), params=dict(self.parameters.items() + parameters.items()), auth=self.auth)
        response.encoding = self.DEFAULT_ENCODING
        if self._has_no_error(response):
            print response.url
            return response.json()

    def get_file(self, url, filename):
        response = requests.get(url, headers=self.headers, auth=self.auth)
        # response.encoding = self.DEFAULT_ENCODING
        if self._has_no_error(response):
            fd = os.open(filename, os.O_CREAT | os.O_RDWR)
            with os.fdopen(fd, "w+b") as f:
                f.write(response.content)

    def post(self, url, data):
        response = requests.post(
            url, headers=self.headers, data=data, auth=self.auth)
        if self._has_no_error(response):
            return response.json()

    def _authenticate(self):
        if self.API_ACCESSTOKENTYPE != "" and self.API_ACCESSTOKEN != "":
            return HSAccessTokenAuth(self.API_ACCESSTOKENTYPE, self.API_ACCESSTOKEN)
        elif self.API_KEY != "":
            return HTTPBasicAuth(self.API_KEY, '')
        elif self.API_EMAIL != "" and self.API_PASSWORD != "":
            return HTTPBasicAuth(self.API_EMAIL, self.API_PASSWORD)
        else:
            raise NoAuthMethod("No Authentication Information Found!")

    def _has_no_error(self, response):
        # If status code is 4xx or 5xx, that should be an error
        if response.status_code >= 400:
            raise HTTPError(str(response.status_code) +
                            " error: " + response.json()["error"]["error_msg"])
        # Return True if everything looks OK
        return True
