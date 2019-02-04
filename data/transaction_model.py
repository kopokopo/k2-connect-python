class transactionDecompose(object):
    def __init__(self,
                 sender_first_name=None,
                 sender_middle_name=None,
                 sender_last_name=None,
                 trans_till=None,
                 trans_amount=None,
                 trans_topic=None,
                 trans_reference=None,
                 trans_orgn_time=None,
                 trans_type=None,
                 json=None):
        self._sender_first_name = sender_first_name
        self._sender_middle_name = sender_middle_name
        self._sender_last_name = sender_last_name
        self._trans_till = trans_till
        self._trans_amount = trans_amount
        self._trans_topic = trans_topic
        self._trans_reference = trans_reference
        self._trans_orgn_time = trans_orgn_time
        self._trans_type = trans_type
        self.json = json

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

    # transaction topic

    @property
    def trans_topic(self):
        return self._trans_topic

    @trans_topic.setter
    def trans_topic(self, value):
        self._trans_topic = value

    @trans_topic.deleter
    def trans_topic(self):
        del self._trans_topic

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

    @property
    def trans_orgn_time(self):
        return self._trans_orgn_time

    @trans_orgn_time.setter
    def trans_orgn_time(self, value):
        self._trans_orgn_time = value

    @trans_orgn_time.deleter
    def trans_orgn_time(self):
        del self._trans_orgn_time

    @property
    def trans_type(self):
        return self._trans_type

    @trans_type.setter
    def trans_type(self, value):
        self._trans_type = value

    @trans_type.deleter
    def trans_type(self):
        del self._trans_type
