"""Handles sending a query to get payment status"""
import requests
from urllib.parse import urljoin


def query_status(payment_request_link):

    # perform GET request
    payment_request_query_resposne = requests.get(url=payment_request_link)

    return payment_request_query_resposne