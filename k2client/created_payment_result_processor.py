"""Handles processing of created payment request"""
import requests
from .request_processor import RequestProcessor


class CreatedPaymentRequestProcessor(object):
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

    def process_created_payment_result(self):
        # inherit webhook processing  method
        created_payment_result = RequestProcessor(self.client_secret,
                                                  self.k2_json_object,
                                                  self.k2_message_body,
                                                  self.k2_headers)

        # process stk push payment request
        processed_created_payment_result = created_payment_result.process()

        return processed_created_payment_result


