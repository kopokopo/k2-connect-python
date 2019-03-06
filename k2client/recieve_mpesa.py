"""Handles reception of payments via sim application toolkit push"""
import requests
import os

from k2client import exceptions
from k2client import validation
from .service import Service
from .query_status import QueryStatus
from .location import ResourceLocation
from .json_builder import subscriber, amount, links, metadata, stk_request

# for sandbox:
# https://api-sandbox.kopokopo.com/payment_requests
# for production:
# https://api.kopokopo.com/payment_requests
receive_mpesa_path = "payment_requests"


class ReceiveMpesaPaymentsService(Service):
    def __init__(self,
                 bearer_token,
                 first_name,
                 last_name,
                 phone,
                 payment_channel,
                 till_identifier,
                 callback_url,
                 value,
                 currency="KES",
                 email=None,
                 **kwargs):
        """
        :param first_name:
        :param last_name:
        :param phone:
        :param payment_channel:
        :param till_identifier:
        :param callback_url:
        :param value:
        :param currency:
        :param email:
        :param kwargs:
        """
        super(ReceiveMpesaPaymentsService, self).__init__(client_id=self._client_id, client_secret=self._client_secret)
        self._bearer_token = bearer_token
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.payment_channel = payment_channel
        self.till_identifier = till_identifier
        self.callback_url = callback_url
        self.email = email
        self.currency = currency
        self.value = value
        self.kwargs = kwargs

    def mpesa_payments_request(self):
        if validation.validate_phone_number(self.phone) is True:
            pass
        elif self.email is not None:
            if validation.validate_email(self.email) is True:
                pass
        else:
            # build url
            url = self.build_url(receive_mpesa_path)

            # define subscriber json object
            payment_subscriber = subscriber(first_name=self.first_name,
                                            last_name=self.last_name,
                                            phone=self.phone,
                                            email=self.email)
            # define amount json object
            payment_amount = amount(self.currency, self.value)

            # define metadata json object (optional)
            metadata_object = {key: value for (key, value) in self.kwargs.items()}
            payment_metadata = metadata(metadata_object)

            # define links json object
            payment_links = links(self.callback_url)

            # define payment request json object
            payload = stk_request(payment_channel=self.payment_channel,
                                  till_identifier=self.till_identifier,
                                  stk_subscriber=payment_subscriber,
                                  stk_amount=payment_amount,
                                  stk_links=payment_links,
                                  stk_metadata=payment_metadata)

            return self.make_requests(url=url, headers=self._headers, method='POST', payload=payload)

    def payment_request_status(self, response):

        # define query location
        query_location = ResourceLocation(response).get_location()

        # define query status object
        query_status_object = QueryStatus(bearer_token=self._bearer_token)

        return query_status_object.query_transaction_status(query_location)



