"""
Handles basic client functionality including HTTP requests

"""
import hmac
import hashlib


class K2_connect_client(object):
    """Performs requests to the Kopo Kopo API web services."""

    def __init__(self, k2_api_token=None):

        """
        :param k2_api_token: Kopo Kopo API key required to interact with the Kopo Kopo library
        :type k2_api_token string
        

        """

        if not k2_api_token:
            raise ValueError("Must provide API key or enterprise credentials when creating client.")

        self.k2_api_token = k2_api_token


def gen_hmac_sig(api_key, msg):
    signature = hmac.new(api_key, msg, hashlib.sha256).hexdigest()
    return signature