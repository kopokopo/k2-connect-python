""""""


class TransactionDecompose(object):
    def __init__(self,
                 # generic event variables
                 sender_first_name=None,
                 sender_middle_name=None,
                 sender_last_name=None,
                 trans_amount=None,
                 trans_currency=None,
                 trans_system=None,
                 trans_status=None,
                 trans_reference=None,
                 trans_orgn_time=None,
                 trans_type=None,

                 # event specific variables
                 trans_till=None,
                 sender_msisdn=None,
                 reversal_time=None,
                 transfer_time=None,
                 transfer_type=None,
                 links_resource=None,
                 links_self=None,
                 links_payment_request=None,

                 # payment request metadata variables
                 payment_request_customer_id=None,
                 payment_request_metadata_reference=None,
                 payment_request_notes=None,

                 # payment request variables
                 payment_request_status=None,

                 # payment request error variables
                 payment_request_error_code=None,
                 payment_request_error_description=None):

        """

        :param sender_first_name:
        :param sender_middle_name:
        :param sender_last_name:
        :param trans_amount:
        :param trans_currency:
        :param trans_system:
        :param trans_status:
        :param trans_reference:
        :param trans_orgn_time:
        :param trans_type:
        :param trans_till:
        :param sender_msisdn:
        :param reversal_time:
        :param transfer_time:
        :param transfer_type:
        :param links_resource:
        :param links_self:
        :param payment_request_customer_id:
        :param payment_request_metadata_reference:
        :param payment_request_notes:
        :param payment_request_status:
        :param payment_request_error_code:
        :param payment_request_error_description:
        """

        self._sender_first_name = sender_first_name
        self._sender_middle_name = sender_middle_name
        self._sender_last_name = sender_last_name
        self._trans_amount = trans_amount
        self._trans_currency = trans_currency
        self._trans_system = trans_system
        self._trans_status = trans_status
        self._trans_reference = trans_reference
        self._trans_orgn_time = trans_orgn_time
        self._trans_type = trans_type
        self._trans_till = trans_till
        self._sender_msisdn = sender_msisdn
        self._reversal_time = reversal_time
        self._transfer_time = transfer_time
        self._transfer_type = transfer_type
        self._links_resource = links_resource
        self._links_self = links_self
        self._links_payment_request = links_payment_request
        self._payment_request_customer_id = payment_request_customer_id
        self._payment_request_metadata_reference = payment_request_metadata_reference
        self._payment_request_notes = payment_request_notes
        self._payment_request_status = payment_request_status
        self._payment_request_error_code = payment_request_error_code
        self._payment_request_error_description = payment_request_error_description

    # first name
    @property
    def sender_first_name(self):
        return self._sender_first_name

    @sender_first_name.setter
    def sender_first_name(self, value):
        self._sender_first_name = value

    @sender_first_name.deleter
    def sender_first_name(self):
        del self._sender_first_name

    # middle name
    @property
    def sender_middle_name(self):
        return self._sender_middle_name

    @sender_middle_name.setter
    def sender_middle_name(self, value):
        self._sender_middle_name = value

    @sender_middle_name.deleter
    def sender_middle_name(self):
        del self._sender_middle_name

    # last name
    @property
    def sender_last_name(self):
        return self._sender_last_name

    @sender_last_name.setter
    def sender_last_name(self, value):
        self._sender_last_name = value

    @sender_last_name.deleter
    def sender_last_name(self):
        del self._sender_last_name

    # transaction amount
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        self._trans_amount = value

    @trans_amount.deleter
    def trans_amount(self):
        del self._trans_amount

    # transaction currency
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value

    @trans_currency.deleter
    def trans_currency(self):
        del self._trans_currency

    # transaction system
    @property
    def trans_system(self):
        return self._trans_system

    @trans_system.setter
    def trans_system(self, value):
        self._trans_system = value

    @trans_system.deleter
    def trans_system(self):
        del self._trans_system

    # transaction status
    @property
    def trans_status(self):
        return self._trans_status

    @trans_status.setter
    def trans_status(self, value):
        self._trans_status = value

    @trans_status.deleter
    def trans_status(self):
        del self._trans_status

    # transaction reference
    @property
    def trans_reference(self):
        return self._trans_reference

    @trans_reference.setter
    def trans_reference(self, value):
        self._trans_reference = value

    @trans_reference.deleter
    def trans_reference(self):
        del self._trans_reference

    # transaction origination time
    @property
    def trans_orgn_time(self):
        return self._trans_orgn_time

    @trans_orgn_time.setter
    def trans_orgn_time(self, value):
        self._trans_orgn_time = value

    @trans_orgn_time.deleter
    def trans_orgn_time(self):
        del self._trans_orgn_time

    # transaction type
    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value

    @trans_type.deleter
    def trans_type(self):
        del self._trans_type

    # till number
    @property
    def trans_till(self):
        return self._trans_till

    @trans_till.setter
    def trans_till(self, value):
        self._trans_till = value

    @trans_till.deleter
    def trans_till(self):
        del self._trans_till

    # sender_msisdn
    @property
    def sender_msisdn(self):
        return self._sender_msisdn

    @sender_msisdn.setter
    def sender_msisdn(self, value):
        self._sender_msisdn = value

    @sender_msisdn.deleter
    def sender_msisdn(self):
        del self._sender_msisdn

    # reversal_time
    @property
    def reversal_time(self):
        return self._reversal_time

    @reversal_time.setter
    def reversal_time(self, value):
        self._reversal_time = value

    @reversal_time.deleter
    def reversal_time(self):
        del self._reversal_time

    # transfer_time
    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value

    @transfer_time.deleter
    def transfer_time(self):
        del self._transfer_time

    # transfer_type
    @property
    def transfer_type(self):
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        self._transfer_type = value

    @transfer_type.deleter
    def transfer_type(self):
        del self._transfer_type

    # links resource
    @property
    def links_resource(self):
        return self._links_resource

    @links_resource.setter
    def links_resource(self, value):
        self._links_resource = value

    @links_resource.deleter
    def links_resource(self):
        del self._links_resource

    # links self
    @property
    def links_self(self):
        return self._links_self

    @links_self.setter
    def links_self(self, value):
        self._links_self = value

    @links_self.deleter
    def links_self(self):
        del self._links_self

    # links_payment_request
    @property
    def links_payment_request(self):
        return self._links_payment_request

    @links_payment_request.setter
    def links_payment_request(self, value):
        self._links_payment_request = value

    @links_payment_request.deleter
    def links_payment_request(self):
        del self._links_payment_request


    # payment_request_customer_id
    @property
    def payment_request_customer_id(self):
        return self._payment_request_customer_id

    @payment_request_customer_id.setter
    def payment_request_customer_id(self, value):
        self._payment_request_customer_id = value

    @payment_request_customer_id.deleter
    def payment_request_customer_id(self):
        del self._payment_request_customer_id

    # payment_request_metadata_reference
    @property
    def payment_request_metadata_reference(self):
        return self._payment_request_metadata_reference

    @payment_request_metadata_reference.setter
    def payment_request_metadata_reference(self, value):
        self._payment_request_metadata_reference = value

    @payment_request_metadata_reference.deleter
    def payment_request_metadata_reference(self):
        del self._payment_request_metadata_reference

    # payment_request_notes
    @property
    def payment_request_notes(self):
        return self._payment_request_notes

    @payment_request_notes.setter
    def payment_request_notes(self, value):
        self._payment_request_notes = value

    @payment_request_notes.deleter
    def payment_request_notes(self):
        del self._payment_request_notes

    # payment_request_status
    @property
    def payment_request_status(self):
        return self._payment_request_status

    @payment_request_status.setter
    def payment_request_status(self, value):
        self._payment_request_status = value

    @payment_request_status.deleter
    def payment_request_status(self):
        del self._payment_request_status

    # payment_request_error_code
    @property
    def payment_request_error_code(self):
        return self._payment_request_error_code

    @payment_request_error_code.setter
    def payment_request_error_code(self, value):
        self._payment_request_error_code = value

    @payment_request_error_code.deleter
    def payment_request_error_code(self):
        del self._payment_request_error_code

    # payment_request_error_description
    @property
    def payment_request_error_description(self):
        return self._payment_request_error_description

    @payment_request_error_description.setter
    def payment_request_error_description(self, value):
        self._payment_request_error_description = value

    @payment_request_error_description.deleter
    def payment_request_error_description(self):
        del self._payment_request_error_description