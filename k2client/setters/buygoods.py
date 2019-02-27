"""Handles getters and setters for buygoods specific result payloads"""


class BuyGoods(object):
    def __init__(self,
                 till_number=None,
                 reversal_time=None,
                 system=None):
        self._till_number = till_number
        self._reversal_time = reversal_time
        self._system = system

    # till number
    @property
    def till_number(self):
        return self._till_number

    @till_number.setter
    def till_number(self, value):
        self._till_number = value

    # reversal_time
    @property
    def reversal_time(self):
        return self._reversal_time

    @reversal_time.setter
    def reversal_time(self, value):
        self._reversal_time = value

    @property
    def system(self):
        return self._system

    @system.setter
    def system(self, value):
        self._system = value