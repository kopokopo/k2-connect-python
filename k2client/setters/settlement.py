"""Handles getters and setter for settlement transfers"""


class SettlementTransfer(object):
    def __init__(self,
                 transfer_time=None,
                 transfer_type=None,
                 destination_type=None,
                 transfer_mode=None,
                 bank=None,
                 branch=None,
                 account_number=None):
        """
        :param transfer_time:
        :param transfer_type:
        :param destination_type:
        :param transfer_mode:
        :param bank:
        :param branch:
        :param account_number:
        """

        self._transfer_time = transfer_time
        self._transfer_type = transfer_type
        self._destination_type = destination_type
        self._transfer_mode = transfer_mode
        self._bank = bank
        self._branch = branch
        self.account_number = account_number

        # transfer_time

    @property
    def transfer_time(self):
        return self._transfer_time

    @transfer_time.setter
    def transfer_time(self, value):
        self._transfer_time = value

    # transfer_type
    @property
    def transfer_type(self):
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, value):
        self._transfer_type = value

    # destination_type
    @property
    def destination_type(self):
        return self._destination_type

    @destination_type.setter
    def destination_type(self, value):
        self._destination_type = value

    # transfer_mode
    @property
    def transfer_mode(self):
        return self._transfer_mode

    @transfer_mode.setter
    def transfer_mode(self, value):
        self._transfer_mode = value

    # bank
    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, value):
        self._bank = value

    # branch
    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, value):
        self._branch = value

    # account_number
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number= value