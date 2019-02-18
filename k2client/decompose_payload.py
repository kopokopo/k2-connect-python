"""Handles breaking down the payload into its constituent elements of data """
from .transaction_model import TransactionDecompose


class PayLoadData(object):

    def __init__(self, payload_json):

        """
        :param payload_json: The authorized JSON from object from Kopo Kopo
        :type payload_json: json
        """
        self.payload_json = payload_json

    def decompose(self):
        # TODO: Find way to clear repetition
        decomposer = TransactionDecompose()
        decomposer.trans_type = self.payload_json['event']['type']
        decomposer_prefix = self.payload_json['event']['resource']
        decomposer.sender_first_name = decomposer_prefix['sender_first_name']
        decomposer.sender_middle_name = decomposer_prefix['sender_middle_name']
        decomposer.sender_last_name = decomposer_prefix['sender_last_name']
        decomposer.trans_amount = decomposer_prefix['amount']
        decomposer.trans_currency = decomposer_prefix['currency']
        decomposer.trans_system = decomposer_prefix['system']
        decomposer.trans_status = decomposer_prefix['status']
        decomposer.trans_reference = decomposer_prefix['reference']
        decomposer.trans_orgn_time = decomposer_prefix['origination_time']

        # event specific variables
        decomposer.trans_till = decomposer_prefix['till_number']
        decomposer.sender_msisdn = decomposer_prefix['sender_msisdn']
        decomposer.reversal_time = decomposer_prefix['reversal_time']
        decomposer.transfer_time = decomposer_prefix['transfer_time']
        decomposer.transfer_type = decomposer_prefix['transfer_type']

        # event link variables
        decomposer.links_self = self.payload_json['_links']['self']
        decomposer.links_resource = self.payload_json['_links']['resource']

        # payment request variables
        decomposer.payment_request_customer_id = self.payload_json['metadata']['customer_id']
        decomposer.payment_request_metadata_reference = self.payload_json['metadata']['reference']
        decomposer.payment_request_notes = self.payload_json['metadata']['notes']
        decomposer.payment_request_status = self.payload_json['status']
        decomposer.payment_request_error_code = self.payload_json['errors']['code']
        decomposer.payment_request_error_description = self.payload_json['errors']['description']

        return decomposer