from k2connect.base_service import BaseService
from k2connect.models.webhook.webhook_subscription_request import WebhookSubscriptionRequest


class K2WebhookSubscriptionService(BaseService):

    def __init__(self, base_url, access_token=None):
        super(K2WebhookSubscriptionService, self).__init__(base_url, access_token)
        self._access_token = access_token

    def create_subscription(self, kwargs):
        webhook_subscription_url = self._build_url(WebhookSubscriptionRequest.endpoint())

        headers = dict(self._headers)

        webhook_subscription_request = WebhookSubscriptionRequest(**kwargs)
        webhook_subscription_request_payload = webhook_subscription_request.request_payload()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=webhook_subscription_url,
                                  payload=webhook_subscription_request_payload)
