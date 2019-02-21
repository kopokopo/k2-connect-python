"""Handles basic client functionality including HTTP requests"""
import hmac
import hashlib
import json


class RequestProcessor(object):
    """Performs requests to the Kopo Kopo API web services."""

    def __init__(self, client_secret=None, k2_json_object=None, k2_message_body=None, k2_headers=None):
        """
        :param client_secret: Your application's client secret
        :type client_secret str

        :param k2_headers: The headers from the POST request received from the webhook's payload
        :type k2_headers: headers

        :param k2_json_object: The collected JSON object from the webhook's payload
        :type k2_json_object: json

        """

        self.client_secret = client_secret
        self.k2_message_body = k2_message_body
        self.k2_headers = k2_headers
        self.k2_json_object = k2_json_object

        if client_secret is None:
            raise ValueError("Must provide client secret or enterprise credentials when creating client.")

    """Confirm JSON object is from KopoKopo"""

    def process(self):
        if self.k2_json_object is None:
            raise ValueError("No JSON Object was received")
        elif self.k2_headers is None:
            raise ValueError("No header file was received")
        elif self.k2_message_body is None:
            raise ValueError("No Message body was recieved")
        else:

            # generate hmac hash
            hash_key = generate_hmac_signature(bytes(self.client_secret, 'utf-8'), self.k2_message_body)

            # get payload signature
            payload_sign = self.k2_headers.get('X-KopoKopo-Signature')

            # compare signatures and raise errors if different
            if hmac.compare_digest(hash_key, payload_sign) is False:
                print(hash_key, payload_sign)
                raise ValueError(" The object delivered is not from KopoKopo ")
            else:
                print(self.k2_json_object)
                return self.k2_json_object


"""
Generates hmac hash to compare with the KopoKopo signature in the payload's header file
"""


def generate_hmac_signature(api_key, message):
    signature = hmac.new(api_key, message, hashlib.sha256).hexdigest()
    return signature
