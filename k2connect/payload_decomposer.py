"""
This module is responsible for the processing of payloads in k2-connect.
It converts JSON objects to python dictionaries then breaks down the python
dictionaries and sets their values to predefined "names" that correspond to
their respective keys in the JSON object using python properties.
:Example:
    sample_dictionary = {'key': 'value'}
    instance_of_payload_decomposer.key = sample_dictionary['value']
"""
import json
from k2connect import exceptions
from k2connect import k2_model
from k2connect import validation

B2B_TRANSACTION_RECEIVED = 'B2b Transaction'
BUYGOODS_TRANSACTION_RECEIVED = 'Buygoods Transaction'
BUYGOODS_TRANSACTION_REVERSED = 'Buygoods Transaction Reversed'
CREATE_PAYMENT = 'pay_request'
CUSTOMER_CREATED = 'Customer Created'
MERCHANT_TO_MERCHANT_TRANSACTION_RECEIVED = 'Merchant to Merchant Transaction'
RECEIVE_PAYMENTS = 'Payment Request'
SETTLEMENT_TRANSFER_COMPLETED = 'Settlement'


def decompose(json_payload):
    """
    Returns an instance of the K2Model class. The decomposer object is used to
    set values that are then accessible through python properties of the same name
    as the setters.
    Example:
        For the JSON object:
        x = {
             "resource": {
                "sender_first_name": "Tyrion",
                "sender_last_name": "Lanister"
                }
            }


        >>>from k2connect import k2_model
        >>>decomposer = k2_model.K2Model()
        >>>resource_payload_nest = payload_dictionary['event']['resource']
        >>>decomposer.first_name = resource_payload_nest['sender_first_name']
        test
        >>> print(decomposer.first_name)
        'Tyrion'

    :param json_payload: A JSON formatted str object
    :type json_payload: str
    """

    validation.validate_string_arguments(json_payload)

    # convert json object to python dictionary for decomposing
    payload_dictionary = json.loads(json_payload)

    # validate dictionary
    validation.validate_dictionary_arguments(payload_dictionary)

    # define result type
    result_type = payload_dictionary['event']['type']

    # define create pay topic
    result_topic = payload_dictionary['topic']

    # define decomposer
    decomposer = k2_model.K2Model()

    resource_payload_nest = payload_dictionary['event']['resource']
    error_payload_nest = payload_dictionary['event']['errors']
    links_payload_nest = payload_dictionary['_links']

    # decompose all values that are similar in webhooks
    if result_type == BUYGOODS_TRANSACTION_RECEIVED \
            or result_type == BUYGOODS_TRANSACTION_REVERSED \
            or result_type == RECEIVE_PAYMENTS:

        decomposer.first_name = resource_payload_nest['sender_first_name']
        decomposer.middle_name = resource_payload_nest['sender_middle_name']
        decomposer.last_name = resource_payload_nest['sender_last_name']
        decomposer.amount = resource_payload_nest['amount']
        decomposer.currency = resource_payload_nest['currency']
        decomposer.system = resource_payload_nest['system']
        decomposer.status = resource_payload_nest['status']
        decomposer.reference = resource_payload_nest['reference']
        decomposer.origination_time = resource_payload_nest['origination_time']

    elif result_type == B2B_TRANSACTION_RECEIVED \
            or result_type == BUYGOODS_TRANSACTION_RECEIVED \
            or result_type == BUYGOODS_TRANSACTION_REVERSED \
            or result_topic == CREATE_PAYMENT\
            or result_type == CUSTOMER_CREATED\
            or result_type == MERCHANT_TO_MERCHANT_TRANSACTION_RECEIVED \
            or result_type == RECEIVE_PAYMENTS\
            or result_type == SETTLEMENT_TRANSFER_COMPLETED:
        decomposer.id = payload_dictionary['id']
        decomposer.resourceId = payload_dictionary['resourceId']

    # decompose all values that have similar links structures
    elif result_type == BUYGOODS_TRANSACTION_REVERSED \
            or result_type == BUYGOODS_TRANSACTION_RECEIVED \
            or result_type == SETTLEMENT_TRANSFER_COMPLETED \
            or result_type == CUSTOMER_CREATED \
            or result_type == B2B_TRANSACTION_RECEIVED \
            or result_type == MERCHANT_TO_MERCHANT_TRANSACTION_RECEIVED:
        decomposer.links_self = links_payload_nest['self']
        decomposer.links_resource = links_payload_nest['resource']

    # decompose all values that are common to buygoods transactions
    elif result_type == BUYGOODS_TRANSACTION_REVERSED \
            or result_type == BUYGOODS_TRANSACTION_RECEIVED:
        decomposer.till_number = resource_payload_nest['till_number']
        decomposer.system = resource_payload_nest['system']

        # decompose value specific to buygoods transaction reversed
        if result_type == BUYGOODS_TRANSACTION_REVERSED:
            decomposer.reversal_time = resource_payload_nest['reversal_time']

    # decompose all values that are common to receive MPESA payments service
    elif result_type == RECEIVE_PAYMENTS:
        # receive MPESA payments
        decomposer.payment_result_id = payload_dictionary['payment_request_id']
        decomposer.payment_result_status = payload_dictionary['status']
        #  receive MPESA payments errors
        decomposer.error_code = error_payload_nest['code']
        decomposer.error_description = error_payload_nest['description']

        # receive MPESA payments links
        decomposer.payment_request = links_payload_nest['payment_request']

    # decompose all values that are common to the PAY service
    elif result_topic == CREATE_PAYMENT:
        decomposer.amount = payload_dictionary['amount']['value']
        decomposer.currency = payload_dictionary['amount']['currency']
        decomposer.status = payload_dictionary['status']
        decomposer.reference = payload_dictionary['reference']
        decomposer.origination_time = payload_dictionary['origination_time']
        decomposer.destination = payload_dictionary['destination']

    # decompose values common to b2b and merchant to merchant transaction received
    elif result_type == B2B_TRANSACTION_RECEIVED \
            or result_type == MERCHANT_TO_MERCHANT_TRANSACTION_RECEIVED:
        decomposer.amount = resource_payload_nest['amount']
        decomposer.currency = resource_payload_nest['currency']
        decomposer.system = resource_payload_nest['system']
        decomposer.status = resource_payload_nest['status']
        decomposer.reference = resource_payload_nest['reference']
        decomposer.origination_time = resource_payload_nest['origination_time']

    # decompose unique to b2b transaction received
    elif result_type == B2B_TRANSACTION_RECEIVED:
        decomposer.sending_till = resource_payload_nest['sending_till']

    # decompose unique to merchant to merchant transaction received
    elif result_type == MERCHANT_TO_MERCHANT_TRANSACTION_RECEIVED:
        decomposer.sending_merchant = resource_payload_nest['sending_merchant']

    return decomposer
