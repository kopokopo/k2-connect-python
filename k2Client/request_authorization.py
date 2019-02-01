"""Handles basic client functionality including HTTP requests"""
import hmac
import hashlib
import os
import json


class request_authorization(object):
    """Performs requests to the Kopo Kopo API web services."""

    def __init__(self, client_secret=None, k2_headers=None, k2_json_object=None):
        """
        :param client_secret: Your application's client secret
        :type client_secret str

        :param k2_headers: The headers from the POST request received from the webhook's payload
        :type k2_headers: headers

        :param k2_json_object: The collected JSON object from the webhook's payload
        :type k2_json_object: json

        """

        self.client_secret = client_secret
        self.k2_headers = k2_headers
        self.k2_json_object = k2_json_object

        if client_secret is None:
            raise ValueError("Must provide client secret or enterprise credentials when creating client.")

    """Confirm JSON object is from KopoKopo"""

    def object_authorization(self):
        if self.k2_json_object is None:
            raise ValueError("No JSON Object was received")
        elif self.k2_headers is None:
            raise ValueError("No header file was received")
        else:

            # convert JSON object into bytes for hashing
            message_body = json.dumps(self.k2_json_object)

            # generate hmac hash
            hash_key = gen_hmac_sig(bytes(self.client_secret, 'utf-8'), message_body.encode('utf-8'))

            # get payload signature
            payload_sign = self.k2_headers.get(os.getenv('X-KopoKopo-Signature'))

            # compare signatures and raise errors if different
            if hmac.compare_digest(hash_key, payload_sign) is False:
                raise ValueError(" The object delivered is not from KopoKopo ")
            else:
                return self.k2_json_object


"""
Generates hmac hash to compare with the KopoKopo signature in the payload's header file
"""


def gen_hmac_sig(api_key, message):
    signature = hmac.new(api_key, message, hashlib.sha256).hexdigest()
    return signature
