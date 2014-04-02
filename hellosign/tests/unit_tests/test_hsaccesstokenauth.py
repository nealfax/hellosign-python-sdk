from unittest import TestCase
from hellosign.utils.hsaccesstokenauth import HSAccessTokenAuth
from hellosign.utils.request import HSRequest


class TestHSAccessTokenAuth(TestCase):

    def test_init(self):
        auth = HSAccessTokenAuth(
            access_token="369c76ae6185f3b7",
            access_token_type="Bearer",
            refresh_token="6a8949c799991e12dac70cb135095680",
            expires_in=10000, state="demo")
        self.assertEquals(auth.access_token, "369c76ae6185f3b7")
        self.assertEquals(auth.access_token_type, "Bearer")
        self.assertEquals(auth.refresh_token,
                          "6a8949c799991e12dac70cb135095680")
        self.assertEquals(auth.expires_in, 10000)
        self.assertEquals(auth.state, "demo")

    def test_call(self):
        auth = HSAccessTokenAuth(access_token="at_test",
                                 access_token_type="att_test")
        request = HSRequest(auth)
        response = request.get(url='http://httpbin.org/headers')
        self.assertEquals(response['headers']['Authorization'],
                          'at_test att_test')
