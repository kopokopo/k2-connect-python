import unittest
from k2connect import exceptions
from k2connect import transfers
from k2connect import validation
from k2connect.exceptions import InvalidArgumentError
from tests import SAMPLE_BASE_URL, SAMPLE_BEARER_TOKEN


class TransferTestCase(unittest.TestCase):

    def test_init_method_with_base_url_argument_succeeds(self):
        transfer_service = transfers.TransferService(base_url=SAMPLE_BASE_URL)
        self.assertIsInstance(transfer_service, transfers.TransferService)

    def test_init_method_without_base_url_argument_fails(self):
        self.assertRaises(TypeError, lambda: transfers.TransferService())

    def test_add_bank_settlement_account_succeeds(self):
        self.assertIsNotNone(
            transfers.TransferService(base_url=SAMPLE_BASE_URL).add_bank_settlement_account(
                SAMPLE_BEARER_TOKEN,
                "account_name",
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id"))

    def test_add_bank_settlement_account_with_invalid_params_fails(self):
        with self.assertRaises(TypeError):
            transfers.TransferService(base_url=SAMPLE_BASE_URL).add_bank_settlement_account(
                SAMPLE_BEARER_TOKEN,
                "account_number",
                "settlement_bank_id",
                "settlement_bank_branch_id")

    def test_add_mobile_wallet_settlement_account_succeeds(self):
        self.assertIsNotNone(
            transfers.TransferService(base_url=SAMPLE_BASE_URL).add_mobile_wallet_settlement_account(
                SAMPLE_BEARER_TOKEN,
                "+254712345678",
                "Safaricom"))

    def test_add_mobile_wallet_settlement_account_with_invalid_phone_succeeds(self):
        with self.assertRaises(InvalidArgumentError):
            transfers.TransferService(base_url=SAMPLE_BASE_URL).add_mobile_wallet_settlement_account(
                SAMPLE_BEARER_TOKEN,
                "phone",
                "Safaricom")

    def test_blind_transfer_succeeds(self):
        self.assertIsNotNone(
            transfers.TransferService(base_url=SAMPLE_BASE_URL).settle_funds(
                SAMPLE_BEARER_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300"))

    def test_targeted_transfer_succeeds(self):
        self.assertIsNotNone(
            transfers.TransferService(base_url=SAMPLE_BASE_URL).settle_funds(
                SAMPLE_BEARER_TOKEN,
                'https://webhook.site/437a5819-1a9d-4e96-b403-a6f898e5bed3',
                "3300",
                "target"))

    def test_transfer_transaction_status_succeeds(self):
        self.assertIsNotNone(
            transfers.TransferService(base_url=SAMPLE_BASE_URL).transfer_transaction_status(
                SAMPLE_BEARER_TOKEN,
                'http://localhost:3000/transfer_simulations/57'))
