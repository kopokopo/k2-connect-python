"""Handles getters and setters for metadata in result payloads"""


class Metadata(object):
    def __init__(self,
                 customer_id=None,
                 reference=None,
                 notes=None):
        self._customer_id = customer_id
        self._reference = reference
        self._notes = notes

    # customer_id
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    # reference
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value

    # notes
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value