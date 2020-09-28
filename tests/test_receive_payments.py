import requests
import unittest
from urlvalidator import URLValidator

from k2connect import receive_payments, authorization, json_builder, exceptions, validation
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET, MSG


class ReceivePaymentTestCase(unittest.TestCase):
    # Establish environment
    validate = URLValidator()

    token_service = authorization.TokenService(SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET)
    access_token_request = token_service.request_access_token()
    ACCESS_TOKEN = token_service.get_access_token(access_token_request)

    incoming_payments_obj = receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL)
    header = dict(incoming_payments_obj._headers)
    header['Authorization'] = 'Bearer ' + ACCESS_TOKEN

    def test_init_method_with_base_url_argument_succeeds(self):
        receive_payments_service = receive_payments.ReceivePaymentsService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(receive_payments_service, receive_payments.ReceivePaymentsService)

    def test_init_method_without_base_url_argument_fails(self):
        self.assertRaises(TypeError, lambda: receive_payments.ReceivePaymentsService())

    def test_successful_create_incoming_payment_request(self):
        response = requests.post(
            headers=ReceivePaymentTestCase.header,
            json=json_builder.mpesa_payment(json_builder.links("https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8"),
                                            json_builder.amount('KES', 'python_sdk_value'),
                                            json_builder.subscriber('first_name', 'last_name', "+254712345678", 'Null'),
                                            'payment_channel', '112233'),
            data=None,
            url=ReceivePaymentTestCase.incoming_payments_obj._build_url(receive_payments.CREATE_RECEIVE_MPESA_PAYMENT_PATH))
        self.assertEqual(response.status_code, 201)

    def test_correct_incoming_payment_method_format(self):
        self.assertIsNotNone(
            ReceivePaymentTestCase.incoming_payments_obj.create_payment_request(
                ReceivePaymentTestCase.ACCESS_TOKEN,
                "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
                "stk_first_name",
                "stk_last_name",
                "payment_channel",
                "+254712345678",
                "till_identifier",
                "stk_amount"))

    def test_create_incoming_payment_returns_resource_url(self):
        response = ReceivePaymentTestCase.incoming_payments_obj.create_payment_request(
                ReceivePaymentTestCase.ACCESS_TOKEN,
                "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
                "stk_first_name",
                "stk_last_name",
                "payment_channel",
                "+254712345678",
                "till_identifier",
                "stk_amount")
        self.assertIsNone(ReceivePaymentTestCase.validate(response))

    def test_create_payment_request_with_invalid_params_fails(self):
        with self.assertRaises(TypeError):
            ReceivePaymentTestCase.incoming_payments_obj.create_payment_request(
                ReceivePaymentTestCase.ACCESS_TOKEN,
                "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
                "stk_last_name",
                "payment_channel",
                "stk_phone",
                "till_identifier",
                "stk_amount")

    def test_create_payment_request_with_invalid_phone_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_phone"]):
            ReceivePaymentTestCase.incoming_payments_obj.create_payment_request(
                ReceivePaymentTestCase.ACCESS_TOKEN,
                "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8",
                "stk_first_name",
                "stk_last_name",
                "payment_channel",
                "stk_phone",
                "till_identifier",
                "stk_amount")

    def test_payment_request_status_succeeds(self):
        self.assertIsNotNone(
            ReceivePaymentTestCase.incoming_payments_obj.payment_request_status(
                ReceivePaymentTestCase.ACCESS_TOKEN,
                "https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8"))

    def test_payment_request_status_with_invalid_query_url_fails(self):
        with self.assertRaises(InvalidArgumentError):
            ReceivePaymentTestCase.incoming_payments_obj.payment_request_status(
                ReceivePaymentTestCase.ACCESS_TOKEN,
                'payment/incoming')
