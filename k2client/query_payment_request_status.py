"""Handles sending a query to get payment status"""
import requests
from urllib.parse import urljoin

# https://api-sandbox.kopokopo.com/payment_requests
default_query_payment_status_url = ""


class QueryPaymentRequestStatus(object):

    def __init__(self, payment_request_id=None):
        """
        :param payment_request_id:
        """
        self.payment_request_id = payment_request_id

    def query_status(self):

        # pass payment request if to url as query parameter
        url = urljoin(default_query_payment_status_url, self.payment_request_id)

        # perform GET request
        payment_request_query = requests.get(url)

        return payment_request_query

