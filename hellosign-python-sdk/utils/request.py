import os
import requests
from exception import *


class HSRequest(object):

    DEFAULT_ENCODING = "UTF-8"
    USER_AGENT = "HelloSign Java SDK"
    parameters = {}
    headers = {'User-Agent': USER_AGENT}
    http_status_code = 0

    def __init__(self, auth):
        self.auth = auth

    def get(self, url, headers={}, parameters={}):
        response = requests.get(
            url, headers=dict(self.headers.items() + headers.items()), params=dict(self.parameters.items() + parameters.items()), auth=self.auth)
        # response.encoding = self.DEFAULT_ENCODING
        self.http_status_code = response.status_code
        if self._has_no_error(response):
            print response.url
            return response.json()

    def get_file(self, url, filename, headers={}):
        response = requests.get(url, headers=dict(self.headers.items() + headers.items()), auth=self.auth)
        # response.encoding = self.DEFAULT_ENCODING
        self.http_status_code = response.status_code
        if self._has_no_error(response):
            fd = os.open(filename, os.O_CREAT | os.O_RDWR)
            with os.fdopen(fd, "w+b") as f:
                f.write(response.content)

    def post(self, url, data={}, files=None, headers={}):
        response = requests.post(
            url, headers=dict(self.headers.items() + headers.items()), data=data, auth=self.auth, files=files)
        self.http_status_code = response.status_code
        if self._has_no_error(response):
            return response.json()

    # TODO: use a expected key in returned json, if the returned key does not match, return false...
    def _has_no_error(self, response):
        # If status code is 4xx or 5xx, that should be an error
        if response.status_code >= 400:
            # I intended to return False here but raising a meaningful exception may make senses more.
            raise HTTPError(str(response.status_code) +
                            " error: " + response.json()["error"]["error_msg"])
        # Return True if everything looks OK
        return True

    def get_http_status_code(self):
        return self.http_status_code
