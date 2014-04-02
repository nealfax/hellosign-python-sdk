class HSException(Exception):
    """General exception class

    We use this object to raise exceptions when none of its child classes is
    suitable for use.

    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class NoAuthMethod(HSException):
    """Exception when no authentication information found"""


class HTTPError(HSException):
    """Exception when an HTTP error found"""


class BadRequest(HTTPError):
    """docstring for BadRequest"""


class Unauthorized(HTTPError):
    """docstring for Unthorized"""


class PaymentRequired(HTTPError):
    """docstring for PaymentRequired"""


class Forbidden(HTTPError):
    """docstring for Forbidden"""


class NotFound(HTTPError):
    """docstring for NotFound"""


class MethodNotAllowed(HTTPError):
    """docstring for MethodNotAllowed"""


class NotAcceptable(HTTPError):
    """docstring for NotAcceptable"""


class RequestTimeout(HTTPError):
    """docstring for RequestTimeout"""


class Conflict(HTTPError):
    """docstring for Conflict"""


class Gone(HTTPError):
    """docstring for Gone"""


class RequestURITooLong(HTTPError):
    """docstring for RequestURITooLong"""


class UnsupportedMediaType(HTTPError):
    """docstring for UnsupportedMediaType"""


class RequestedRangeNotSatisfiable(HTTPError):
    """docstring for RequestedRangeNotSatisfiable"""


class InternalServerError(HTTPError):
    """docstring for InternalServerError"""


class MethodNotImplemented(HTTPError):
    """docstring for NotImplemented"""


class BadGateway(HTTPError):
    """docstring for BadGateway"""


class ServiceUnavailable(HTTPError):
    """docstring for ServiceUnavailable"""


class GatewayTimeout(HTTPError):
    """docstring for GatewayTimeout"""


class InvalidEmail(HSException):
    """Exception when an email address is invalid"""


class EmptyPassword(HSException):
    """Exception when a password is empty"""
