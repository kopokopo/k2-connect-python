"""Handles creating an outgoing payment to a third party."""
import requests
from .json_builder import amount, metadata, links, payment_object

# https://api-sandbox.kopokopo.com/payments
default_create_payments_url = ""


def send_pay(destination=None,
             currency=None,
             value=None,
             customer_id=None,
             notes=None,
             callback_url=None):
    # define amount json object
    payment_amount = amount(currency=currency, value=value)

    # define metadata json object
    payment_metadata = metadata(customer_id=customer_id, notes=notes)

    # define links json object
    payment_links = links(links_call_back_url=callback_url)

    # define payment json object for POST request
    payment_object = payment(destination=destination,
                             amount=payment_amount,
                             metadata=payment_metadata,
                             links=payment_links)

    # perform POST request to create payment
    create_payment_request = requests.post(url=default_create_payments_url, json=payment_object)

    return create_payment_request

