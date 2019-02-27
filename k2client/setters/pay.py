"""Handles creation of getters and setters for decomposition of result payloads"""


class PAY(object):
    def __init__(self,
                 destination=None):
        self._destination = destination

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value