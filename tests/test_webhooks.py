import unittest

from urlvalidator import URLValidator

from k2connect import exceptions
from k2connect import webhooks
from k2connect import validation
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_BEARER_TOKEN, SAMPLE_WEBHOOK_SECRET


class WebhooksTestCase(unittest.TestCase):
    validate = URLValidator()

    def test_init_method_with_base_url_argument_succeeds(self):
        webhook_service = webhooks.WebhookService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(webhook_service, webhooks.WebhookService)

    # Test it successfully sends the request
    def test_create_buygoods_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "buygoods_transaction_received",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233'))

    def test_create_b2b_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "b2b_transaction_received",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233'))

    def test_create_buygoods_reversal_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "buygoods_transaction_reversed",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233'))

    def test_create_customer_created_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "customer_created",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233'))

    def test_create_settlement_transfer_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "settlement_transfer_completed",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233'))

    def test_create_m2m_transaction_received_webhook_succeeds(self):
        self.assertIsNotNone(webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "m2m_transaction_received",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233'))

    # Test it returns the resource_url
    def test_buygoods_webhook_subscription_returns_resource_url(self):
        req = webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "buygoods_transaction_received",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233')
        self.assertIsNone(WebhooksTestCase.validate(req))

    def test_b2b_webhook_subscription_returns_resource_url(self):
        req = webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "b2b_transaction_received",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233')
        self.assertIsNone(WebhooksTestCase.validate(req))

    def test_buygoods_reversal_webhook_subscription_returns_resource_url(self):
        req = webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "buygoods_transaction_reversed",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233')
        self.assertIsNone(WebhooksTestCase.validate(req))

    def test_customer_created_webhook_subscription_returns_resource_url(self):
        req = webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "customer_created",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233')
        self.assertIsNone(WebhooksTestCase.validate(req))

    def test_settlement_webhook_subscription_returns_resource_url(self):
        req = webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "settlement_transfer_completed",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233')
        self.assertIsNone(WebhooksTestCase.validate(req))

    def test_m2m_webhook_subscription_returns_resource_url(self):
        req = webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
            SAMPLE_BEARER_TOKEN,
            "m2m_transaction_received",
            "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
            SAMPLE_WEBHOOK_SECRET,
            'Till',
            '112233')
        self.assertIsNone(WebhooksTestCase.validate(req))

    # Test for failure scenarios
    def test_create_invalid_webhook_fails(self):
        with self.assertRaises(InvalidArgumentError):
            webhooks.WebhookService(base_url=SAMPLE_BASE_URL).create_subscription(
                SAMPLE_BEARER_TOKEN,
                "settlement",
                "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
                SAMPLE_WEBHOOK_SECRET,
                'Till',
                '112233')
