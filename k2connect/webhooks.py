"""
This module handles the creation of webhook subscriptions. It creates
a subscription to receive webhooks for a particular event_type.
"""
from k2connect import exceptions
from k2connect import json_builder
from k2connect import service
from k2connect import validation

WEBHOOK_SUBSCRIPTION_PATH = 'api/v1/webhook_subscriptions'


class WebhookService(service.Service):
    """
    The WebhookService class contains methods for the creation of a webhook
    subscription.
    Example:
        # initialize webhook service
        >>> k2-connect.WebhookService
        >>> k2-connect.create_subscription('buygoods_transaction_reversed',
        >>>................................'https://myapplication/webhooks',
        >>>................................os.getenv('SOME_UNCRACKABLE_SECRET'))

    """

    def __init__(self, base_url):
        """
        :param base_url:
        :type  base_url: str
        """
        super(WebhookService, self).__init__(base_url)

    def create_subscription(self,
                            bearer_token,
                            event_type,
                            webhook_endpoint,
                            webhook_secret,
                            scope,
                            scope_reference):
        """
        Creates a subscription to a webhook service.
        Returns a request response object < class, 'requests.models.Response'>
        :param bearer_token: Access token to be used to make calls to
        the Kopo Kopo API
        :type bearer_token: str
        :param event_type:Type of subscription event. Should be one of:
        buygoods_transaction_received, buygoods_transaction_reversed,
        settlement_transfer_completed, customer_created
        :type event_type:  str
        :param webhook_endpoint: HTTP end point to send the webhook.
        :type webhook_endpoint: str
        :param webhook_secret: Secret used to encrypt the request payload using HMAC.
        :type webhook_secret: str
        :param scope: A string that will be used to specify whether account is at Till or Company level.
        :type scope: str
        :param scope_reference: A string that represents the account number (eg MPESA till number).
        :type scope_reference: str
        :return: requests.models.Response
        """
        # event types
        event_types_to_check = ['b2b_transaction_received',
                                'buygoods_transaction_received',
                                'buygoods_transaction_reversed',
                                'm2m_transaction_received',
                                'settlement_transfer_completed',
                                'customer_created'
                                ]
        # build subscription url
        subscription_url = self._build_url(WEBHOOK_SUBSCRIPTION_PATH)

        # define headers
        headers = dict(self._headers)

        # validate string arguments
        validation.validate_string_arguments(bearer_token,
                                             event_type,
                                             webhook_endpoint,
                                             webhook_secret,
                                             scope,
                                             scope_reference)

        headers['Authorization'] = 'Bearer ' + bearer_token + ''

        if not any(check in event_type for check in event_types_to_check):
            raise exceptions.InvalidArgumentError('Event type not recognized by k2-connect')

        # validate webhook endpoint
        validation.validate_url(webhook_endpoint)
        
        # define subscription payload
        subscription_payload = json_builder.webhook_subscription(event_type=event_type,
                                                                 webhook_endpoint=webhook_endpoint,
                                                                 webhook_secret=webhook_secret,
                                                                 scope=scope,
                                                                 scope_reference=scope_reference)

        return self._make_requests(headers=headers,
                                   method='POST',
                                   url=subscription_url,
                                   payload=subscription_payload)

    def webhook_status(self, bearer_token, query_url):
        """
        Returns a JSON object result containing the transaction status.
        :param bearer_token: Access token to be used to make calls to
        the Kopo Kopo API.
        :type bearer_token: str
        :param query_url: URL to which status query is made.
        :type query_url: str
        :return str
        """
        return self._query_transaction_status(bearer_token=bearer_token,
                                              query_url=query_url)
