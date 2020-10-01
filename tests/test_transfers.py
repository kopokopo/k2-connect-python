import requests
import unittest
from urlvalidator import URLValidator
from k2connect import transfers, authorization, json_builder, exceptions, validation
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET


class TransferTestCase(unittest.TestCase):
    verified_settlement_url = ''
    transfer_funds_url = ''
    # Establish environment
    validate = URLValidator()

    token_service = authorization.TokenService(SAMPLE_BASE_URL, SAMPLE_CLIENT_ID, SAMPLE_CLIENT_SECRET)
    access_token_request = token_service.request_access_token()
    ACCESS_TOKEN = token_service.get_access_token(access_token_request)

    settlement_transfer_obj = transfers.TransferService(base_url=SAMPLE_BASE_URL)
    header = dict(settlement_transfer_obj._headers)
    header['Authorization'] = 'Bearer ' + ACCESS_TOKEN

    def test_init_method_with_base_url_argument_succeeds(self):
        transfer_service = transfers.TransferService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(transfer_service, transfers.TransferService)

    def test_init_method_without_base_url_argument_fails(self):
        self.assertRaises(TypeError, lambda: transfers.TransferService())

    # Add Settlement Accounts
    # Bank account
    def test_add_bank_settlement_account_for_RTS_transfer_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.add_bank_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "RTS",
                "account_name",
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id"))

    def test_add_bank_settlement_account_for_EFT_transfer_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.add_bank_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "EFT",
                "account_name",
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id"))

    def test_successful_add_bank_settlement_account_for_EFT_transfer_returns_resource_url(self):
        response = TransferTestCase.settlement_transfer_obj.add_bank_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "EFT",
                "account_name",
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id")
        if self.assertIsNone(TransferTestCase.validate(response)) is None:
            TransferTestCase.verified_settlement_url = response
        self.assertIsNone(TransferTestCase.validate(response))

    def test_successful_add_bank_settlement_account_for_RTS_transfer_returns_resource_url(self):
        response = TransferTestCase.settlement_transfer_obj.add_bank_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "RTS",
                "account_name",
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id")
        if self.assertIsNone(TransferTestCase.validate(response)) is None:
            TransferTestCase.verified_settlement_url = response
        self.assertIsNone(TransferTestCase.validate(response))

    def test_add_bank_settlement_account_for_EFT_transfer_request(self):
        response = requests.post(
            headers=TransferTestCase.header,
            json=json_builder.bank_settlement_account("EFT", "py_sdk_account_name", "py_sdk_account_number", "21",
                                                      "633aa26c-7b7c-4091-ae28-96c0687cf886"),
            data=None,
            url=TransferTestCase.settlement_transfer_obj._build_url(transfers.SETTLEMENT_BANK_ACCOUNTS_PATH))
        self.assertEqual(response.status_code, 201)

    def test_add_bank_settlement_account_for_RTS_transfer_request(self):
        response = requests.post(
            headers=TransferTestCase.header,
            json=json_builder.bank_settlement_account("RTS", "py_sdk_account_name", "py_sdk_account_number", "21",
                                                      "633aa26c-7b7c-4091-ae28-96c0687cf886"),
            data=None,
            url=TransferTestCase.settlement_transfer_obj._build_url(transfers.SETTLEMENT_BANK_ACCOUNTS_PATH))
        self.assertEqual(response.status_code, 201)

    # Failure scenarios
    def test_add_bank_settlement_account_with_invalid_params_fails(self):
        with self.assertRaises(TypeError):
            TransferTestCase.settlement_transfer_obj.add_bank_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id")

    # Mobile Wallet
    def test_add_mobile_wallet_settlement_account_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.add_mobile_wallet_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "py_sdk_first_name",
                "py_sdk_last_name",
                "+254712345678",
                "Safaricom"))

    def test_successful_add_mobile_wallet_settlement_account_returns_resource_url(self):
        response = TransferTestCase.settlement_transfer_obj.add_mobile_wallet_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "py_sdk_first_name",
                "py_sdk_last_name",
                "+254712345678",
                "Safaricom")
        if self.assertIsNone(TransferTestCase.validate(response)) is None:
            TransferTestCase.verified_settlement_url = response
        self.assertIsNone(TransferTestCase.validate(response))

    def test_add_mobile_wallet_settlement_account_request(self):
        response = requests.post(
            headers=TransferTestCase.header,
            json=json_builder.mobile_settlement_account("py_sdk_first_name", "py_sdk_last_name", "254900112502",
                                                        "safaricom"),
            data=None,
            url=TransferTestCase.settlement_transfer_obj._build_url(transfers.SETTLEMENT_MOBILE_ACCOUNTS_PATH))
        self.assertEqual(response.status_code, 201)

    # Failure scenarios
    def test_add_mobile_wallet_settlement_account_with_invalid_phone_succeeds(self):
        with self.assertRaises(InvalidArgumentError):
            TransferTestCase.settlement_transfer_obj.add_mobile_wallet_settlement_account(
                TransferTestCase.ACCESS_TOKEN,
                "py_sdk_first_name",
                "py_sdk_last_name",
                "phone",
                "Safaricom")

    # Transfer/Settle funds
    # Blind Transfer
    def test_blind_transfer_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.settle_funds(
                TransferTestCase.ACCESS_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300"))

    def test_successful_blind_transfer_transaction_returns_resource_url(self):
        response = TransferTestCase.settlement_transfer_obj.settle_funds(
                TransferTestCase.ACCESS_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300")
        if self.assertIsNone(TransferTestCase.validate(response)) is None:
            TransferTestCase.transfer_funds_url = response
        self.assertIsNone(TransferTestCase.validate(response))

    def test_successful_blind_transfer_request(self):
        response = requests.post(
            headers=TransferTestCase.header,
            json=json_builder.transfers(json_builder.links('https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3'),
                                        json_builder.amount('KES', "3300")),
            data=None,
            url=TransferTestCase.settlement_transfer_obj._build_url(transfers.TRANSFER_PATH))
        self.assertEqual(response.status_code, 201)

    # Targeted Transfer
    # Merchant Bank Account
    def test_targeted_transfer_to_merchant_bank_account_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.settle_funds(
                TransferTestCase.ACCESS_TOKEN, 'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300", "merchant_bank_account", "6ad03242-2c6e-4050-8e46-987cb74f5326"))

    def test_successful_targeted_transfer_to_merchant_bank_account_returns_resource_url(self):
        response = TransferTestCase.settlement_transfer_obj.settle_funds(
                TransferTestCase.ACCESS_TOKEN, 'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300", "merchant_bank_account", "6ad03242-2c6e-4050-8e46-987cb74f5326")
        if self.assertIsNone(TransferTestCase.validate(response)) is None:
            TransferTestCase.transfer_funds_url = response
        self.assertIsNone(TransferTestCase.validate(response))

    def test_successful_targeted_transfer_to_merchant_bank_account_request(self):
        response = requests.post(
            headers=TransferTestCase.header,
            json=json_builder.transfers(json_builder.links('https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3'),
                                        json_builder.amount('KES', "3300"),
                                        **{"destination_type": "merchant_bank_account",
                                           "destination_reference": "6ad03242-2c6e-4050-8e46-987cb74f5326"}),
            data=None,
            url=TransferTestCase.settlement_transfer_obj._build_url(transfers.TRANSFER_PATH))
        self.assertEqual(response.status_code, 201)

    # Merchant Wallet
    def test_targeted_transfer_to_merchant_wallet_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.settle_funds(
                TransferTestCase.ACCESS_TOKEN, 'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300", "merchant_wallet", "+254947237528"))

    def test_successful_targeted_transfer_to_merchant_wallet_returns_resource_url(self):
        response = TransferTestCase.settlement_transfer_obj.settle_funds(
                TransferTestCase.ACCESS_TOKEN, 'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300", "merchant_wallet", "+254947237528")
        if self.assertIsNone(TransferTestCase.validate(response)) is None:
            TransferTestCase.transfer_funds_url = response
        self.assertIsNone(TransferTestCase.validate(response))

    def test_successful_targeted_transfer_to_merchant_wallet_request(self):
        response = requests.post(
            headers=TransferTestCase.header,
            json=json_builder.transfers(json_builder.links('https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3'),
                                        json_builder.amount('KES', "3300"),
                                        **{"destination_type": "merchant_wallet",
                                           "destination_reference": "+254947237528"}),
            data=None,
            url=TransferTestCase.settlement_transfer_obj._build_url(transfers.TRANSFER_PATH))
        self.assertEqual(response.status_code, 201)

    # Query Transactions
    # Verified Settlement Account Status
    def test_successfully_added_settlement_account_status_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.transfer_transaction_status(
                TransferTestCase.ACCESS_TOKEN,
                TransferTestCase.verified_settlement_url))

    def test_successfully_added_settlement_account_status_request(self):
        response = requests.get(
            headers=TransferTestCase.header,
            url=TransferTestCase.verified_settlement_url)
        self.assertEqual(response.status_code, 200)

    # Transfer Transaction Status
    def test_successful_transferred_funds_transaction_status_succeeds(self):
        self.assertIsNotNone(
            TransferTestCase.settlement_transfer_obj.transfer_transaction_status(
                TransferTestCase.ACCESS_TOKEN,
                TransferTestCase.transfer_funds_url))

    def test_successful_transferred_funds_transaction_status_request(self):
        response = requests.get(
            headers=TransferTestCase.header,
            url=TransferTestCase.transfer_funds_url)
        self.assertEqual(response.status_code, 200)

    # Failure scenarios
