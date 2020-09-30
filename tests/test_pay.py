import requests
import unittest
from urlvalidator import URLValidator
from k2connect import pay, exceptions, validation, authorization, json_builder
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET, PAY, MSG


class PayTestCase(unittest.TestCase):
    pay_transaction_query_url = ''
    pay_recipient_query_url = ''
    # Establish environment
    validate = URLValidator()

    token_service = authorization.TokenService(SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET)
    access_token_request = token_service.request_access_token()
    ACCESS_TOKEN = token_service.get_access_token(access_token_request)

    pay_obj = pay.PayService(base_url=SAMPLE_BASE_URL)
    header = dict(pay_obj._headers)
    header['Authorization'] = 'Bearer ' + ACCESS_TOKEN

    def test_init_method_with_base_url_argument_succeeds(self):
        pay_service = pay.PayService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(pay_service, pay.PayService)

    def test_init_method_without_base_url_argument_fails(self):
        self.assertRaises(TypeError, lambda: pay.PayService())

    # Mobile Pay recipient
    def test_add_mobile_pay_recipient_succeeds(self):
        self.assertIsNotNone(
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'mobile_wallet', **PAY["mobile_pay"]))

    def test_successful_add_mobile_pay_receipient_request(self):
        response = requests.post(
            headers=PayTestCase.header,
            json=json_builder.pay_recipient("mobile_wallet",
                                            json_builder.mobile_wallet("first_name", "last_name", "254900112501", "safaricom")),
            data=None,
            url=PayTestCase.pay_obj._build_url(pay.ADD_PAY_PATH))
        self.assertEqual(response.status_code, 201)

    def test_add_mobile_pay_recipient_returns_resource_url(self):
        response = PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'mobile_wallet', **PAY["mobile_pay"])
        if self.assertIsNone(PayTestCase.validate(response)) is None:
            PayTestCase.pay_recipient_query_url = response
        self.assertIsNone(PayTestCase.validate(response))

    # Mobile Pay Recipient Failure Scenarios
    def test_add_mobile_pay_recipient_without_first_name_fails(self):
        with self.assertRaises(InvalidArgumentError):
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'mobile_wallet', **PAY["invalid_first_name_mobile_pay"])

    def test_add_mobile_pay_recipient_with_invalid_email_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_email"]):
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'mobile_wallet', **PAY["invalid_email_mobile_pay"])

    def test_add_mobile_pay_recipient_with_invalid_phone_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_phone"]):
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'mobile_wallet', **PAY["invalid_phone_mobile_pay"])

    # Bank Pay recipient
    def test_add_bank_pay_recipient_succeeds(self):
        self.assertIsNotNone(
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'bank_account', **PAY["bank_pay"]))

    def test_successful_add_bank_receipient_request(self):
        response = requests.post(
            headers=PayTestCase.header,
            json=json_builder.pay_recipient("bank_account",
                                            json_builder.bank_account("David Kariuki Python", "566566",
                                                                      "21", "633aa26c-7b7c-4091-ae28-96c0687cf886",
                                                                      "first_name", "last_name",)),
            data=None,
            url=PayTestCase.pay_obj._build_url(pay.ADD_PAY_PATH))
        self.assertEqual(response.status_code, 201)

    def test_add_bank_pay_recipient_returns_resource_url(self):
        response = PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'bank_account', **PAY["bank_pay"])
        if self.assertIsNone(PayTestCase.validate(response)) is None:
            PayTestCase.pay_recipient_query_url = response
        self.assertIsNone(PayTestCase.validate(response))

    # Bank Pay Recipient Failure Scenarios
    def test_add_bank_pay_recipient_without_first_name_fails(self):
        with self.assertRaises(InvalidArgumentError):
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'bank_account', **PAY["invalid_first_name_bank_pay"])

    def test_add_bank_pay_recipient_with_invalid_email_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_email"]):
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'bank_account', **PAY["invalid_email_bank_pay"])

    def test_add_bank_pay_recipient_with_invalid_phone_fails(self):
        with self.assertRaisesRegex(InvalidArgumentError, MSG["invalid_phone"]):
            PayTestCase.pay_obj.add_pay_recipient(
                PayTestCase.ACCESS_TOKEN, 'bank_account', **PAY["invalid_phone_bank_pay"])

    # Send Pay Transaction
    def test_send_pay_to_mobile_wallet_succeeds(self):
        self.assertIsNotNone(PayTestCase.pay_obj.send_pay(
            PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132", "mobile_wallet",
            'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3', "3300"))

    def test_create_pay_to_bank_account_succeeds(self):
        self.assertIsNotNone(PayTestCase.pay_obj.send_pay(
            PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132", "bank_account",
            'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3', "3300"))

    def test_create_pay_to_mobile_wallet_returns_resource_url(self):
        response = PayTestCase.pay_obj.send_pay(
            PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132", "mobile_wallet",
            'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3', "3300")
        if self.assertIsNone(PayTestCase.validate(response)) is None:
            PayTestCase.pay_transaction_query_url = response
        self.assertIsNone(PayTestCase.validate(response))

    def test_create_pay_to_bank_account_returns_resource_url(self):
        response = PayTestCase.pay_obj.send_pay(
            PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132", "bank_account",
            'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3', "3300")
        if self.assertIsNone(PayTestCase.validate(response)) is None:
            PayTestCase.pay_transaction_query_url = response
        self.assertIsNone(PayTestCase.validate(response))

    def test_successful_create_pay_request_to_mobile_wallet(self):
        response = requests.post(
            headers=PayTestCase.header,
            json=json_builder.pay("3344-effefnkka-132", "mobile_wallet", json_builder.amount('KES', 'python_sdk_value'),
                                  json_builder.links("https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8"),
                                  json_builder.metadata({"cId": '8_675_309', "notes": 'Salary payment May 2018'})),
            data=None,
            url=PayTestCase.pay_obj._build_url(pay.SEND_PAY_PATH))
        self.assertEqual(response.status_code, 201)

    def test_successful_create_pay_request_to_bank_account(self):
        response = requests.post(
            headers=PayTestCase.header,
            json=json_builder.pay("3344-effefnkka-132", "bank_account", json_builder.amount('KES', 'python_sdk_value'),
                                  json_builder.links("https://webhook.site/dcbdce14-dd4f-4493-be2c-ad3526354fa8"),
                                  json_builder.metadata({"cId": '8_675_309', "notes": 'Salary payment May 2018'})),
            data=None,
            url=PayTestCase.pay_obj._build_url(pay.SEND_PAY_PATH))
        self.assertEqual(response.status_code, 201)

    # Send Pay Transaction Failure Scenarios
    def test_send_pay_without_destination_reference_fails(self):
        with self.assertRaises(TypeError):
            PayTestCase.pay_obj.send_pay(PayTestCase.ACCESS_TOKEN, "bank_account",
                                         'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3', "3300")

    def test_send_pay_without_destination_type_fails(self):
        with self.assertRaises(TypeError):
            PayTestCase.pay_obj.send_pay(PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132",
                                         'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3', "3300")

    def test_send_pay_without_value_fails(self):
        with self.assertRaises(TypeError):
            PayTestCase.pay_obj.send_pay(PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132", "bank_account",
                                         'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3')

    def test_send_pay_with_invalid_callback_fails(self):
        with self.assertRaises(InvalidArgumentError):
            PayTestCase.pay_obj.send_pay(PayTestCase.ACCESS_TOKEN, "3344-effefnkka-132", "bank_account", 'callback',
                                         "3300")

    # Query Status
    # Query Pay Transaction
    def test_pay_transaction_status_succeeds(self):
        self.assertIsNotNone(PayTestCase.pay_obj.pay_transaction_status(PayTestCase.ACCESS_TOKEN,
                                                                        PayTestCase.pay_transaction_query_url))

    def test_pay_transaction_request_status_returns_object(self):
        self.assertIsNotNone(PayTestCase.pay_obj.pay_transaction_status(PayTestCase.ACCESS_TOKEN,
                                                                        PayTestCase.pay_transaction_query_url))

    def test_successful_query_pay_transaction_request(self):
        response = requests.get(
            headers=PayTestCase.header,
            url=PayTestCase.pay_transaction_query_url)
        self.assertEqual(response.status_code, 200)

    # Query Pay Recipient
    def test_pay_recipient_request_status_returns_object(self):
        self.assertIsNotNone(PayTestCase.pay_obj.pay_transaction_status(PayTestCase.ACCESS_TOKEN,
                                                                        PayTestCase.pay_recipient_query_url))

    def test_successful_query_pay_recipient_request(self):
        response = requests.get(
            headers=PayTestCase.header,
            url=PayTestCase.pay_recipient_query_url)
        self.assertEqual(response.status_code, 200)

    # Query Status Failure Scenarios
    def test_pay_transaction_status_with_invalid_query_url_fails(self):
        with self.assertRaises(InvalidArgumentError):
            PayTestCase.pay_obj.pay_transaction_status(
                PayTestCase.ACCESS_TOKEN, "destination")

    def test_pay_transaction_status_with_invalid_access_token_fails(self):
        with self.assertRaises(InvalidArgumentError):
            PayTestCase.pay_obj.pay_transaction_status(
                'access_token', "destination")

