"""Handles getters and setters for error in result payoads"""


class Errors(object):

    def __init__(self,
                 error_code=None,
                 error_description=None):

        self._error_code = error_code
        self._error_description = error_description

    # error_code
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value

    # error_description
    @property
    def error_description(self):
        return self._error_description

    @error_description.setter
    def error_description(self, value):
        self._error_description = value