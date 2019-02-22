"""Handles breaking down transaction payloads into their constituent elements of data """

from .properties_setters.k2_result import Result

# define result type space
buygoods_transaction_received = 'buygoods_transaction_received'
buygoods_transaction_reversed = 'buygoods_transaction_reversed'
settlement_transfer_completed = 'settlement_transfer_completed'
customer_created = 'customer_created'
recieve_payments = 'payment_request'
# revisit for topic
create_payment = ''


class ResultPayload(Result):
    def __init__(self, result_payload):
        self.decomposer = super().__init__()
        self.result_payload = result_payload

    # function to breakdown transaction payloads
    def decompose_result(self):
        # define result type
        result_type = self.result_payload['topic']

        # access resource nest
        resource_payload_nest = self.result_payload['event']['resource']

        # access error nest
        error_payload_nest = self.result_payload['event']['errors']

        # access metadata nest
        metadata_payload_nest = self.result_payload['metadata']

        # access links nest
        links_payload_nest = self.result_payload['_links']

        # check transaction payload type
        if result_type is buygoods_transaction_received or buygoods_transaction_reversed or recieve_payments:
            # decompose webhook generic values
            self.decomposer.first_name = resource_payload_nest['sender_first_name']
            self.decomposer.middle_name = resource_payload_nest['sender_middle_name']
            self.decomposer.last_name = resource_payload_nest['sender_last_name']
            self.decomposer.amount = resource_payload_nest['amount']
            self.decomposer.currency = resource_payload_nest['currency']
            self.decomposer.system = resource_payload_nest['system']
            self.decomposer.status = resource_payload_nest['status']
            self.decomposer.reference = resource_payload_nest['reference']
            self.decomposer.orgn_time = resource_payload_nest['origination_time']

        elif result_type is buygoods_transaction_reversed or buygoods_transaction_received:
            # decompose buygoods generic values
            self.decomposer.till_number = resource_payload_nest['till_number']
            self.decomposer.system = resource_payload_nest['system']

            # decompose buygoods transaction reversed specific value
            if result_type is buygoods_transaction_reversed:
                self.decomposer.reversal_time = resource_payload_nest['reversal_time']

        elif result_type is recieve_payments:
            # recieve MPESA payment
            self.decomposer.payment_result_id = self.result_payload['payment_request_id']
            self.decomposer.payment_result_status = self.result_payload['status']

            #  recieve MPESA payment errors
            self.decomposer.error_code = error_payload_nest['code']
            self.decomposer.error_description = error_payload_nest['description']

            # recieve MPESA payment metadata
            self.decomposer.customer_id = metadata_payload_nest['customer_id']
            self.decomposer.reference = metadata_payload_nest['reference']
            self.decomposer.notes = metadata_payload_nest['notes']

            # recieve MPESA payment links
            self.decomposer.payment_request = links_payload_nest['payment_request']
            self.decomposer.links_resource = links_payload_nest['resource']
            self.decomposer.links_self = links_payload_nest['self']

        elif result_type is create_payment:
            # decompose PAY generic values
            self.decomposer.amount = self.result_payload['amount']['value']
            self.decomposer.currency = self.result_payload['amount']['currency']
            self.decomposer.status = self.result_payload['status']
            self.decomposer.reference = self.result_payload['reference']
            self.decomposer.orgn_time = self.result_payload['origination_time']
            self.decomposer.destination = self.result_payload['destination']

            # decompose PAY metadata
            self.decomposer.customer_id = metadata_payload_nest['customer_id']
            self.decomposer.notes = metadata_payload_nest['notes']

            # decompose PAY links
            self.decomposer.links_self = links_payload_nest['self']

        return self.decomposer


data = {
    "id": "cac95329-9fa5-42f1-a4fc-c08af7b868fb",
    "resourceId": "",
    "topic": "payment_request",
    "created_at": "2018-06-20T22:45:12.790Z",
    "status": "Failed",
    "event": {
        "type": "Payment Request",
        "resource": "",
        "errors": [
            {
                "code": "501",
                "description": "Insufficient funds"
            }
        ]
    },
    "metadata": {
        "customer_id": "123456789",
        "reference": "123456",
        "notes": "Payment for invoice 123456"
    },
    "_links": {
        "self": "https://api-sandbox.kopokopo.com/payment_request_results/cac95329-9fa5-42f1-a4fc-c08af7b868fb",
        "payment_request": "https://api-sandbox.kopokopo.com/payment_requests/cac95329-9fa5-42f1-a4fc-c08af7b868fb"
    }
}

values = ResultPayload(data).decompose_result()

print(values.payment_request)