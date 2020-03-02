import unittest
from k2connect import exceptions
from k2connect import webhooks
from k2connect import validation
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_BEARER_TOKEN, SAMPLE_CLIENT_SECRET


class WebhooksTestCase(unittest.TestCase):

    def test_init_method_with_base_url_argument_succeeds(self):
        webhook_service = webhooks.WebhookService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(webhook_service, webhooks.WebhookService)

    def test_create_buygoods_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "buygoods_transaction_received",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET))

    def test_create_b2b_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "b2b_transaction_received",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET))

    def test_create_buygoods_reversal_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "buygoods_transaction_reversed",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET))

    def test_create_customer_created_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "customer_created",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET))

    def test_create_settlement_transfer_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "settlement_transfer_completed",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET))

    def test_create_m2m_transaction_received_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "m2m_transaction_received",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET))

    def test_create_invalid_webhook_fails(self):
        with self.assertRaises(InvalidArgumentError):
            webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "settlement",
            "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3",
            SAMPLE_CLIENT_SECRET)
