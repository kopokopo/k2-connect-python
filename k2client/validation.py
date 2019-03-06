"""Handles validation of expected user inputs"""
import re
from urllib.parse import urlparse
from k2client import exceptions


def validate_email(email):
    """
    :param email: An email address
    :type email: str
    :return: True
    """
    validated_email = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
    if validated_email is not None:
        return True
    else:
        raise exceptions.InvalidArgumentError("The email address passed is invalid. (Should be: email@domain.com)")


def validate_phone_number(phone_number):
    """
    :param phone_number: A phone number
    :type phone_number: str
    :return: True
    """
    validated_phone_number = re.search('^\+\d{1,3}\d{3,}$', phone_number)
    if validated_phone_number is not None:
        return True
    else:
        raise exceptions.InvalidArgumentError('The phone number passed is invalid. (Should be: +254123456789)')


def validate_url(url):
    validated_url = urlparse(url)
    # check url format
    if validated_url.scheme is "" or validated_url.netloc is "":
        raise exceptions.InvalidArgumentError('The url format passed is invalid (should be : https://domain.com)')
    elif validated_url.scheme is not "" and not validated_url.scheme == 'https':
        raise exceptions.InvalidArgumentError('Provide a url with a valid certificate => (https://)')
    else:
        return True