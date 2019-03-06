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
    def __init__(self, event_type, callback_url, webhook_secret):
        """
        :param event_type:
        :param callback_url:
        :param webhook_secret:
        """
        super(WebhookService).__init__(client_id=self._client_secret, client_secret=self._client)
        self.event_type = event_type
        self.callback_url = callback_url
        self.webhook_secret = webhook_secret

    # create webhook subscription
    def create_subscription(self, event_type, callback_url, webhook_secret, bearer_token):
        # bearer token to use for subscription creation
        self._bearer_token = bearer_token

        # event types
        event_types_to_check = ['buygoods_transaction_received',
                                'buygoods_transaction_reversed',
                                'settlement_transfer_completed',
                                'customer_created']

        if event_type or callback_url or webhook_secret is None:
            raise exceptions.ValueEmptyError
        elif not any(check in event_type for check in event_types_to_check):
            raise exceptions.InvalidEventTypeError
        elif not callable(callback_url):
            raise exceptions.InvalidCallbackURL('Invalid callback_url')
        else:
            try:
                # set request body
                payload = webhook_subscription(self.event_type,
                                               self.callback_url,
                                               self.webhook_secret)
                # build url
                url = self.build_url(webhook_subscription_path)
            except exceptions.InvalidEventTypeError:
                print("Enter a valid event type")
            else:
                # perform POST request
                subscription_response = self.make_requests(headers=self._headers, method='POST', url=url, payload=payload)
                return subscription_response


