from requests.auth import AuthBase


class HSAccessTokenAuth(AuthBase):

    def __init__(self, access_token, access_token_type):
        # setup any auth-related data here
        self.access_token = access_token
        self.access_token_type = access_token_type

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = self.access_token_type + \
            ' ' + self.access_token
        return r
