"""Handles getters and setters for metadata in result payloads"""


class Metadata(object):
    def __init__(self,
                 customer_id=None,
                 metadata_reference=None,
                 notes=None):
        self._customer_id = customer_id
        self._metadata_reference = metadata_reference
        self._notes = notes

    # customer_id
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    # metadata_reference
    @property
    def metadata_reference(self):
        return self._metadata_reference

    @metadata_reference.setter
    def metadata_reference(self, value):
        self._metadata_reference = value

    # notes
    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value