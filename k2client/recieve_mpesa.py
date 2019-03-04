"""Handles reception of payments via sim application toolkit push"""
import requests
import os

from .json_builder import subscriber, amount, links, metadata, stk_request

# https://api-sandbox.kopokopo.com/payment_requests
default_stk_push_url = ""


def stk_service(payment_channel=None,
                till_identifier=None,
                first_name=None,
                last_name=None,
                phone=None,
                email=None,
                currency="KES",
                value=None,
                customer_id=None,
                reference=None,
                notes=None,
                call_back_url=None):
    # define subscriber json object
    payment_subscriber = subscriber(first_name=first_name,
                                    last_name=last_name,
                                    phone=phone,
                                    email=email)
    # define amount json object
    payment_amount = amount(currency, value)

    # define metadata json object (optional)
    payment_metadata = metadata(customer_id=customer_id,
                                reference=reference,
                                notes=notes)

    # define links json object
    payment_links = links(call_back_url)

    # define payment request json object
    payload = stk_request(payment_channel=payment_channel,
                          till_identifier=till_identifier,
                          stk_subscriber=payment_subscriber,
                          stk_amount=payment_amount,
                          stk_links=payment_links,
                          stk_metadata=payment_metadata)

    # define headers
    headers = {'content-type': 'application/vnd.kopokopo.v4.hal+json',
               'accept': 'application/vnd.kopokopo.v4.hal+json'}

    # perform post request
    payment_post_request = requests.post(url=post_url, payload=payload, headers=headers)

    return payment_post_request
