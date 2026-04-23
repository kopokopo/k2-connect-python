import json
import unittest

from k2connect import payload_decomposer

DARAJA_PAYLOAD = {
    "TransactionType": "Pay Bill",
    "TransID": "LGR219G3EY",
    "TransTime": "20170727104247",
    "TransAmount": "10.00",
    "BusinessShortCode": "600610",
    "BillRefNumber": "account",
    "InvoiceNumber": "",
    "OrgAccountBalance": "49197.00",
    "ThirdPartyTransId": "",
    "MSISDN": "254901234567",
    "FirstName": "John",
    "MiddleName": "",
    "LastName": "Doe",
}


class DarajaPayloadDecomposerTestCase(unittest.TestCase):
    def setUp(self):
        self.result = payload_decomposer.decompose(json.dumps(DARAJA_PAYLOAD))

    def test_daraja_payload_sets_topic_to_daraja_payload(self):
        self.assertEqual(self.result.topic, payload_decomposer.DARAJA_PAYLOAD)

    def test_daraja_payload_decomposes_transaction_type(self):
        self.assertEqual(self.result.transaction_type, "Pay Bill")

    def test_daraja_payload_decomposes_transaction_id(self):
        self.assertEqual(self.result.transaction_id, "LGR219G3EY")

    def test_daraja_payload_decomposes_transaction_time(self):
        self.assertEqual(self.result.transaction_time, "20170727104247")

    def test_daraja_payload_decomposes_transaction_amount(self):
        self.assertEqual(self.result.transaction_amount, "10.00")

    def test_daraja_payload_decomposes_business_short_code(self):
        self.assertEqual(self.result.business_short_code, "600610")

    def test_daraja_payload_decomposes_bill_ref_number(self):
        self.assertEqual(self.result.bill_ref_number, "account")

    def test_daraja_payload_decomposes_invoice_number(self):
        self.assertEqual(self.result.invoice_number, "")

    def test_daraja_payload_decomposes_org_account_balance(self):
        self.assertEqual(self.result.org_account_balance, "49197.00")

    def test_daraja_payload_decomposes_third_party_transaction_id(self):
        self.assertEqual(self.result.third_party_transaction_id, "")

    def test_daraja_payload_decomposes_msisdn(self):
        self.assertEqual(self.result.msisdn, "254901234567")

    def test_daraja_payload_decomposes_first_name(self):
        self.assertEqual(self.result.first_name, "John")

    def test_daraja_payload_decomposes_middle_name(self):
        self.assertEqual(self.result.middle_name, "")

    def test_daraja_payload_decomposes_last_name(self):
        self.assertEqual(self.result.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
