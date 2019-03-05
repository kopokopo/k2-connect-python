"""Handles custom exceptions"""


# TODO: Make more generic
class K2Error(Exception):
    """Base exception for all errors raised by the K2-Connect library"""

    def __init__(self, error=None):
        if error is None:
            # default error message
            error = "An error has occurred  in the k2-connect library"
        super(K2Error, self).__init__(error)


class ValueEmptyError(K2Error, TypeError):
    """Value cannot be empty"""
    pass


class InvalidEventTypeError(K2Error, TypeError):
    """The event type passed is not a k2 defined event type"""
    pass


class InvalidTypeError(K2Error, ValueError):
    """The value passed was of an invalid type"""
    pass


class InsecureURLError(K2Error):
    """An insecure url is passed"""
    pass


class InvalidRequestMethodError(K2Error):
    """The method passed is not recognized by k2-connect"""
    pass


class InvalidArgumentError(K2Error):
    """The argument passed is invalid, pass message to error description"""