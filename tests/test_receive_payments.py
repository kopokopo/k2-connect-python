import unittest
from k2connect import exceptions
from k2connect import validation
from k2connect import receive_payments
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_BEARER_TOKEN, MSG


class ReceivePaymentTestCase(unittest.TestCase):

    def test_init_method_with_base_url_argument_succeeds(self):
        receive_payments_service = receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(receive_payments_service, receive_payments.ReceivePaymentsService)

    def test_init_method_without_base_url_argument_fails(self):
        self.assertRaises(TypeError, lambda: receive_payments.ReceivePaymentsService())

    def test_create_payment_request_succeeds(self):
        self.assertIsNotNone(
            receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL).create_payment_request(
                SAMPLE_BEARER_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "stk_first_name",
                "stk_last_name",
                "payment_channel",
                "+254712345678",
                "till_identifier",
                "stk_amount"))

    def test_create_payment_request_with_invalid_params_fails(self):
        with self.assertRaises(TypeError):
            receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL).create_payment_request(
                SAMPLE_BEARER_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "stk_last_name",
                "payment_channel",
                "stk_phone",
                "till_identifier",
                "stk_amount")

    def test_create_payment_request_with_invalid_phone_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_phone"]):
            receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL).create_payment_request(
                SAMPLE_BEARER_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "stk_first_name",
                "stk_last_name",
                "payment_channel",
                "stk_phone",
                "till_identifier",
                "stk_amount")

    def test_payment_request_status_succeeds(self):
        self.assertIsNotNone(
            receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL).payment_request_status(
                SAMPLE_BEARER_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3'))

    def test_payment_request_status_with_invalid_query_url_fails(self):
        with self.assertRaises(InvalidArgumentError):
            receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL).payment_request_status(
                SAMPLE_BEARER_TOKEN,
                'payment/incoming')
