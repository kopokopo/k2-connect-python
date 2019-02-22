""" Handles creation of getters and setters for the decomposition of transaction payloads"""
from .k2_metadata import Metadata
from .k2_links import Links
from .k2_errors import Errors
from .pay import PAY
from .payment_result import PaymentResult
from .buygoods import BuyGoods
from .settlement import SettlementTransfer


class Result(Errors, PAY, BuyGoods, SettlementTransfer, Metadata, Links):

    def __init__(self, first_name=None, middle_name=None, last_name=None, amount=None, currency=None, status=None,
                 reference=None, orgn_time=None, msisdn=None):

        """
        :param first_name:
        :param middle_name:
        :param last_name:
        :param amount:
        :param currency:
        :param status:
        :param reference:
        :param orgn_time:
        :param msisdn:
        """

        super().__init__()
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._amount = amount
        self._currency = currency
        self._status = status
        self._reference = reference
        self._orgn_time = orgn_time
        self._msisdn = msisdn

    # first name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # middle name
    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    # last name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # transaction value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    # transaction currency
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    # transaction status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    # transaction reference
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value

    # transaction origination time
    @property
    def orgn_time(self):
        return self._orgn_time

    @orgn_time.setter
    def orgn_time(self, value):
        self._orgn_time = value

    # msisdn
    @property
    def msisdn(self):
        return self._msisdn

    @msisdn.setter
    def msisdn(self, value):
        self._msisdn = value




