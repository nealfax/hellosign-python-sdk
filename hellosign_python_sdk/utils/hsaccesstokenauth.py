from requests.auth import AuthBase


class HSAccessTokenAuth(AuthBase):
    """Authentication object using HelloSign's access token

    """

    def __init__(self, access_token, access_token_type):
        """Initialziation of the object

        Args:
            access_token (str): Access token
            access_token_type (str): Access token type

        """

        self.access_token = access_token
        self.access_token_type = access_token_type

    def __call__(self, r):
        r.headers['Authorization'] = self.access_token_type + \
            ' ' + self.access_token
        return r
