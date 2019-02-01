"""Handles breaking down the payload into its constituent elements of data """
from data.buy_goods_transactions import buy_goods_transaction_decompose


class pay_load_data(object):

    def __init__(self, payload_json):

        """
        :param payload_json: The authorized JSON from object from Kopo Kopo
        :type payload_json: json
        """
        self.payload_json = payload_json

    def decompose(self):
        # TODO: Find way to clear repetition
        decomposer = buy_goods_transaction_decompose()
        decomposer.sender_first_name = self.payload_json['event']['resource']['sender_first_name']
        decomposer.sender_middle_name = self.payload_json['event']['resource']['sender_middle_name']
        decomposer.sender_last_name = self.payload_json['event']['resource']['sender_last_name']
        decomposer.trans_till = self.payload_json['event']['resource']['till_number']
        decomposer.trans_amount = self.payload_json['event']['resource']['amount']
        decomposer.trans_topic = self.payload_json['topic']
        decomposer.trans_reference = self.payload_json['event']['resource']['reference']
        decomposer.trans_orgn_time = self.payload_json['event']['resource']['origination_time']
        decomposer.trans_type = self.payload_json['event']['resource']['system']

        return decomposer