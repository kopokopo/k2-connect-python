"""Handles sending a query to get payment status"""
import requests
from urllib.parse import urljoin

# https://api-sandbox.kopokopo.com/payment_requests
default_query_stk_push_payment_status_url = ""


class QuerySTKPushPaymentRequestStatus(object):

    def __init__(self, stk_push_payment_request_id=None):
        """
        :param payment_request_id:
        """
        self.stk_push_payment_request_id = stk_push_payment_request_id

    def query_status(self):

        # pass payment request if to url as query parameter
        url = urljoin(default_query_stk_push_payment_status_url, self.stk_push_payment_request_id)

        # perform GET request
        stk_push_payment_request_query_resposne = requests.get(url)

        return stk_push_payment_request_query_resposne

