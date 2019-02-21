"""Handles creating an outgoing payment to a third party."""
import requests

# https://api-sandbox.kopokopo.com/payments
default_create_payments_url = ""


class CreatePayment(object):
    def __init__(self,
                 destination=None,
                 currency=None,
                 value=None,
                 customer_id=None,
                 notes=None,
                 callback_url=None):

        """
        :param destination:
        :param currency:
        :param value:
        :param customer_id:
        :param notes:
        :param callback_url:
        """

        self.destination = destination
        self.currency = currency
        self.value = value
        self.customer_id = customer_id
        self.notes = notes
        self.callback_url = callback_url

    def create_payment(self):
        # define amount json object
        amount = payment_amount_json_object_builder(provided_currency=self.currency, provided_value=self.value)

        # define metadata json object
        metadata = payment_metadata_json_object_builder(provided_customer_id=self.customer_id,
                                                        provided_notes=self.notes)

        # define links json object
        links = payment_links_json_object_builder(self.callback_url)

        # define payment json object for POST request
        payment_json_object = payment_json_object_builder(provided_destination=self.destination,
                                                          provided_amount=amount,
                                                          provided_metadata=metadata,
                                                          provided_links=links)

        # perform POST request to create payment
        create_payment_request = requests.post(url=default_create_payments_url, json=payment_json_object)

        return create_payment_request


# build amount json object
def payment_amount_json_object_builder(provided_currency, provided_value):
    payment_amount_json_object = {
        "currency": provided_currency,
        "value": provided_value
    }
    return payment_amount_json_object


# build metadata json object
def payment_metadata_json_object_builder(provided_customer_id, provided_notes):
    payment_metadata_json_object = {
        "customer_id": provided_customer_id,
        "notes": provided_notes
    }
    return payment_metadata_json_object


# build links json object
def payment_links_json_object_builder(provided_callback_url):
    payment_links_json_object = {
        "callback_url": provided_callback_url
    }
    return payment_links_json_object


# build payment json object
def payment_json_object_builder(provided_destination,
                                provided_amount,
                                provided_metadata,
                                provided_links):

    payment_json_object = {
        "destination": provided_destination,
        "amount": provided_amount,
        "metadata": provided_metadata,
        "_links": provided_links
    }
    return payment_json_object


# payment request location
def location(response):
    payment_data_location = response.headers.get('location')
    return payment_data_location