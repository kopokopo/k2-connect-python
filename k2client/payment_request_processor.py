"""Handles processing the an initiated payment request response"""
from .webhook_processor import RequestAuthorization


class ResponseAuthentication(object):
    def __init__(self, client_secret=None, k2_json_object=None, k2_message_body=None, k2_headers=None):
        """

        :param client_secret:
        :param k2_json_object:
        :param k2_message_body:
        :param k2_headers:
        """
        self.client_secret = client_secret
        self.k2_message_body = k2_message_body
        self.k2_headers = k2_headers
        self.k2_json_object = k2_json_object

    def process_payment_request_response(self):

        # inherit webhook processing authorization process
        payment_request_response = RequestAuthorization(self.client_secret,
                                                        self.k2_json_object,
                                                        self.k2_message_body,
                                                        self.k2_headers)

        # authorize payment_request_response
        authorized_payment_request = payment_request_response.authorize()

        return authorized_payment_request
