import unittest
from k2connect import exceptions
from k2connect import pay
from k2connect import validation
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_BEARER_TOKEN, PAY, MSG


class PayTestCase(unittest.TestCase):

    def test_init_method_with_base_url_argument_succeeds(self):
        pay_service = pay.PayService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(pay_service, pay.PayService)

    def test_init_method_without_base_url_argument_fails(self):
        self.assertRaises(TypeError, lambda: pay.PayService())

    def test_add_mobile_pay_recipient_succeeds(self):
        self.assertIsNotNone(
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'mobile_wallet', **PAY["mobile_pay"]))

    def test_add_mobile_pay_recipient_without_first_name_fails(self):
        with self.assertRaises(InvalidArgumentError):
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'mobile_wallet', **PAY["invalid_first_name_mobile_pay"])

    def test_add_mobile_pay_recipient_with_invalid_email_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_email"]):
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'mobile_wallet', **PAY["invalid_email_mobile_pay"])

    def test_add_mobile_pay_recipient_with_invalid_phone_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_phone"]):
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'mobile_wallet', **PAY["invalid_phone_mobile_pay"])

    def test_add_bank_pay_recipient_succeeds(self):
        self.assertIsNotNone(
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'bank_account', **PAY["bank_pay"]))

    def test_add_bank_pay_recipient_without_first_name_fails(self):
        with self.assertRaises(InvalidArgumentError):
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'bank_account', **PAY["invalid_first_name_bank_pay"])

    def test_add_bank_pay_recipient_with_invalid_email_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_email"]):
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'bank_account', **PAY["invalid_email_bank_pay"])

    def test_add_bank_pay_recipient_with_invalid_phone_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_phone"]):
            pay.PayService(base_url=SAMPLE_BASE_URL).add_pay_recipient(
                SAMPLE_BEARER_TOKEN, 'bank_account', **PAY["invalid_phone_bank_pay"])

    def test_send_pay_succeeds(self):
        self.assertIsNotNone(pay.PayService(base_url=SAMPLE_BASE_URL).send_pay(
            SAMPLE_BEARER_TOKEN, 'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
            "destination",
            "3300"))

    def test_send_pay_with_invalid_callback_fails(self):
        with self.assertRaises(InvalidArgumentError):
            pay.PayService(base_url=SAMPLE_BASE_URL).send_pay(
                SAMPLE_BEARER_TOKEN,
                'callback',
                "destination",
                "3300")

    def test_pay_transaction_status_succeeds(self):
        self.assertIsNotNone(pay.PayService(base_url=SAMPLE_BASE_URL).pay_transaction_status(
            SAMPLE_BEARER_TOKEN, "https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3"))

    def test_pay_transaction_status_with_invalid_query_url_fails(self):
        with self.assertRaises(InvalidArgumentError):
            pay.PayService(base_url=SAMPLE_BASE_URL).pay_transaction_status(
                SAMPLE_BEARER_TOKEN, "destination")
