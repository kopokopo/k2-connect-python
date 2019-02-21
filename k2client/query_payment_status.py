"""Handles sending a query to get payment status"""
import requests
from urllib.parse import urljoin

# https://api-sandbox.kopokopo.com/payment_requests
default_query_stk_push_payment_status_url = ""


class PaymentRequestStatus(object):
    def __init__(self, payment_request_id=None):
        """
        :param payment_request_id:
        """
        self.payment_request_id = payment_request_id

    def query_status(self):
        # perform GET request
        payment_request_query_resposne = requests.get(url=default_query_stk_push_payment_status_url,
                                                      params=self.payment_request_id)
        return payment_request_query_resposne