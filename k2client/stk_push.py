"""Handles reception of payments via sim application toolkit push"""
import requests
import os

from .json_builder import subscriber, amount, links, metadata

# https://api-sandbox.kopokopo.com/payment_requests
default_stk_push_url = ""


class StkPush(object):

    def __init__(self,
                 payment_channel=None,
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
        """
        :param payment_channel:
        :param till_identifier:
        :param first_name:
        :param last_name:
        :param phone:
        :param email:
        :param currency:
        :param value:
        :param customer_id:
        :param reference:
        :param notes:
        :param call_back_url:
        """
        self.payment_channel = payment_channel
        self.till_identifier = till_identifier
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.currency = currency
        self.value = value
        self.customer_id = customer_id
        self.reference = reference
        self.notes = notes
        self.call_back_url = call_back_url

    def payment_post_requst(self):
        # define subscriber json object
        subscriber = subscriber(provided_first_name=self.first_name,
                                provided_last_name=self.last_name,
                                provided_phone=self.phone,
                                provided_email=self.email)
        # define amount json object
        amount = amount(self.currency, self.value)

        # define metadata json object (optional)
        metadata = metadata(provided_customer_id=self.customer_id,
                            provided_reference=self.reference,
                            provided_notes=self.notes)

        # define links json object
        links = links(self.call_back_url)

        # define payment request json object
        payload = payment_request_json_object_builder(provided_payment_channel=self.payment_channel,
                                                      provided_till_identifier=self.till_identifier,
                                                      provided_subscriber=subscriber,
                                                      provided_amount=amount,
                                                      provided_links=links,
                                                      provided_metadata=metadata)

        # define headers
        headers = {'content-type': 'application/vnd.kopokopo.v4.hal+json',
                   'accept': 'application/vnd.kopokopo.v4.hal+json'}

        # perform post request
        payment_post_request = requests.post(url=self.post_url, payload=payload, headers=headers)

        return payment_post_request


# post request location
def location(response):
    payment_data_location = response.headers.get('location')
    return payment_data_location
