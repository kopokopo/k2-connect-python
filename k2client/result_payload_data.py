"""Handles breaking down transaction payloads into their constituent elements of data """

from k2client.setters import k2_result

# define result type space
buygoods_transaction_received = 'buygoods_transaction_received'
buygoods_transaction_reversed = 'buygoods_transaction_reversed'
settlement_transfer_completed = 'settlement_transfer_completed'
customer_created = 'customer_created'
recieve_payments = 'payment_request'
# revisit for topic
create_payment = 'create_payment'


class ResultPayload(object):
    def __init__(self, json_payload):
        self.json_payload = json_payload

    def decompose(self):
        # define decomposer
        decomposer = k2_result.Result()

        # define result type
        result_type = self.json_payload['topic']

        # access resource nest
        resource_payload_nest = self.result_payload['event']['resource']

        # access error nest
        error_payload_nest = self.result_payload['event']['errors']

        # access metadata nest
        metadata_payload_nest = self.result_payload['metadata']

        # access links nest
        links_payload_nest = self.result_payload['_links']

        # decompose all values that are similar in webhooks
        if result_type is buygoods_transaction_received or buygoods_transaction_reversed or recieve_payments:

            decomposer.first_name = resource_payload_nest['sender_first_name']
            decomposer.middle_name = resource_payload_nest['sender_middle_name']
            decomposer.last_name = resource_payload_nest['sender_last_name']
            decomposer.amount = resource_payload_nest['amount']
            decomposer.currency = resource_payload_nest['currency']
            decomposer.system = resource_payload_nest['system']
            decomposer.status = resource_payload_nest['status']
            decomposer.reference = resource_payload_nest['reference']
            decomposer.orgn_time = resource_payload_nest['origination_time']

        # decompose all values that have similar metadata structures
        elif result_type is recieve_payments or create_payment:
            decomposer.metadata_customer_id = metadata_payload_nest['customer_id']
            decomposer.metadata_reference = metadata_payload_nest['reference']

        # decompose all values that have similar links structures
        elif result_type is buygoods_transaction_reversed \
                or buygoods_transaction_received \
                or settlement_transfer_completed \
                or customer_created:
            decomposer.links_self = links_payload_nest['self']
            decomposer.links_resource = links_payload_nest['resource']

        # decompose all values that are common to buygoods transactions
        elif result_type is buygoods_transaction_reversed or buygoods_transaction_received:
            decomposer.till_number = resource_payload_nest['till_number']
            decomposer.system = resource_payload_nest['system']

            # decompose value specific to buygoods transaction reversed
            if result_type is buygoods_transaction_reversed:
                decomposer.reversal_time = resource_payload_nest['reversal_time']

        # decompose all values that are common to recieve MPESA payments service
        elif result_type is recieve_payments:
            # recieve MPESA payment
            decomposer.payment_result_id = self.result_payload['payment_request_id']
            decomposer.payment_result_status = self.result_payload['status']
            #  recieve MPESA payment errors
            decomposer.error_code = error_payload_nest['code']
            decomposer.error_description = error_payload_nest['description']
            # recieve MPESA payment metadata
            decomposer.metadata_notes = metadata_payload_nest['notes']
            # recieve MPESA payment links
            decomposer.payment_request = links_payload_nest['payment_request']

        # decompose all values that are common to the PAY service
        elif result_type is create_payment:
            decomposer.amount = self.result_payload['amount']['value']
            decomposer.currency = self.result_payload['amount']['currency']
            decomposer.status = self.result_payload['status']
            decomposer.reference = self.result_payload['reference']
            decomposer.orgn_time = self.result_payload['origination_time']
            decomposer.destination = self.result_payload['destination']

            # decompose PAY metadata
            decomposer.notes = metadata_payload_nest['notes']

            return decomposer



