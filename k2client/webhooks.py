""" Handles subscription to webhook services"""
import os
from k2client import exceptions

from .json_builder import webhook_subscription
from .service import Service

# for sandbox:
# https://api-sandbox.kopokopo.com/webhook-subscription
# for production:
# https://api.kopokopo.com/webhook-subscription
webhook_subscription_path = "webhook-subscription"


class WebhookService(Service):
    def __init__(self, bearer_token):
        """
        :param bearer_token: Access token to be used to make calls to the Kopo Kopo API
        :type  bearer_token: str
        """
        super(WebhookService).__init__(client_id=self._client_secret, client_secret=self._client)
        self._bearer_token = bearer_token

    # create webhook subscription
    def create_subscription(self, event_type, webhook_endpoint, webhook_secret):
        """
        :param event_type:The type of event you are subscribing to. Should be one of; buygoods_transaction_received, buygoods_transaction_reversed, settlement_transfer_completed, customer_created
        :type event_type:  str
        :param webhook_endpoint: The http end point to send the webhook. MUST be secured with HTTPS (TLS)
        :type webhook_endpoint: str
        :param webhook_secret: A string that will be used to encrypt the request payload using HMAC
        :type webhook_secret: str
        :return: Http response object
        """
        # event types
        event_types_to_check = ['buygoods_transaction_received',
                                'buygoods_transaction_reversed',
                                'settlement_transfer_completed',
                                'customer_created']

        if event_type or webhook_endpoint or webhook_secret is None:
            raise exceptions.ValueEmptyError
        elif not any(check in event_type for check in event_types_to_check):
            raise exceptions.InvalidEventTypeError
        elif not callable(webhook_endpoint):
            raise exceptions.InvalidCallbackURL('Invalid webhook_endpoint')
        else:
            try:
                # set request body
                payload = webhook_subscription(event_type,
                                               webhook_endpoint,
                                               webhook_secret)
                # build url
                url = self.build_url(webhook_subscription_path)
            except exceptions.InvalidEventTypeError:
                print("Enter a valid event type")
            else:
                # perform POST request
                subscription_response = self.make_requests(headers=self._headers, method='POST', url=url, payload=payload)
                return subscription_response


