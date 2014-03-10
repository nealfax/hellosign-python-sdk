class HSException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NoAuthMethod(HSException):
    """docstring for NoAuthMethod"""


class HTTPError(HSException):
    """docstring for HTTPError"""


class InvalidEmail(HSException):
    """docstring for InvalidEmail"""


class EmptyPassword(HSException):
    """docstring for EmptyPassword"""
