"""Handles reception of payments via sim application toolkit push"""
import requests
import os


class StkPush(object):
    # Default URL.
    default_stk_push_url = os.getenv('DEFAULT_STK_PUSH_URL')

    def __init__(self,
                 post_url=default_stk_push_url,
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
        self.post_url = post_url
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
        subscriber = subscriber_json_object_builder(self.first_name,
                                                    self.last_name,
                                                    self.phone,
                                                    self.email)
        # define amount json object
        amount = amount_json_object_builder(self.currency, self.value)

        # define metadata json object (optional)
        metadata = metadata_json_object_builder(self.customer_id,
                                                self.reference,
                                                self.notes)

        # define links json object
        links = links_json_object_builder(self.call_back_url)

        # define payment request json object
        payload = payment_request_json_object_builder(self.payment_channel,
                                                      self.till_identifier,
                                                      subscriber,
                                                      amount,
                                                      links,
                                                      metadata)

        # define headers
        headers = {'content-type': 'application/vnd.kopokopo.v4.hal+json',
                   'accept': 'application/vnd.kopokopo.v4.hal+json'}

        # perform post request
        payment_post_request = requests.post(self.post_url, payload, headers)

        return payment_post_request


# build subscriber json object
def subscriber_json_object_builder(provided_first_name, provided_last_name, provided_phone, provided_email):
    subscriber_json_object = "{\"first_name\":\"" + provided_first_name + "\",""\"last_name\":\"" + provided_last_name + "\",""\"phone\":\"" + provided_phone + "\",""\"email\":\"" + provided_email + "\"}"
    return subscriber_json_object


# build amount json object
def amount_json_object_builder(provided_currency, provided_value):
    amount_json_object = "{\"currency\":\"" + provided_currency + "\",""\"amount\":\"" + provided_value + "\"}"
    return amount_json_object


# build metadata json object
def metadata_json_object_builder(provided_customer_id, provided_reference, provided_notes):
    metadata_json_object = "{\"customer_id\":\"" + provided_customer_id + "\",""\"reference\":\"" + provided_reference + "\",""\"notes\":\"" + provided_notes + "\"}"
    return metadata_json_object


# build links json object
def links_json_object_builder(provided_call_back_url):
    links_json_object = "{\"call_back_url\":\"" + provided_call_back_url + "\"}"
    return links_json_object


# build payment request json object
def payment_request_json_object_builder(provided_payment_channel, provided_till_identifier, provided_subscriber,
                                        provided_amount, provided_links, provided_metadata=None):
    payment_request_json_object = "{\"payment_channel\":\"" + provided_payment_channel + "\",""\"till_identifier\":\"" + provided_till_identifier + "\",""\"subscriber\":\"" + provided_subscriber + "\",""\"amount\":\"" + provided_amount + "\",""\"metadata\":\"" + provided_metadata + "\",""\"links\":\"" + provided_links + "\"}"
    return payment_request_json_object


# post request location
def location(response):
    payment_data_location = response.headers.get('location')
    return payment_data_location
