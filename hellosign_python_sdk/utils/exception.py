class HSException(Exception):
    """General exception class

    We use this object to raise exceptions when none of its child classes is
    suitable for use.

    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NoAuthMethod(HSException):
    """Exception when no authentication information found"""


class HTTPError(HSException):
    """Exception when an HTTP error found"""


class InvalidEmail(HSException):
    """Exception when an email address is invalid"""


class EmptyPassword(HSException):
    """Exception when a password is empty"""
