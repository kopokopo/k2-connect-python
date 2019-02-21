"""Handles processing the result initiated payment request"""
from .request_processor import RequestProcessor


class RequestedPaymentProcessor(object):
    def __init__(self,
                 client_secret=None,
                 k2_json_object=None,
                 k2_message_body=None,
                 k2_headers=None):
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

    def process_stk_push_payment_result(self):
        # inherit webhook processing authorization process
        payment_request_result = RequestProcessor(self.client_secret,
                                                  self.k2_json_object,
                                                  self.k2_message_body,
                                                  self.k2_headers)

        # process stk push payment request
        processed_stk_push_payment_result = payment_request_result.process()

        return processed_stk_push_payment_result
