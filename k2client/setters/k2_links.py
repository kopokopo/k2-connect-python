"""Handles getters and setters for links in result payloads"""


class Links(object):
    def __init__(self,
                 links_resource=None,
                 links_self=None,
                 payment_request=None,):
        self._links_resource = links_resource
        self._links_self = links_self
        self._payment_request = payment_request

        # links resource

    @property
    def links_resource(self):
        return self._links_resource

    @links_resource.setter
    def links_resource(self, value):
        self._links_resource = value

    # links self
    @property
    def links_self(self):
        return self._links_self

    @links_self.setter
    def links_self(self, value):
        self._links_self = value

    # payment_request_links
    @property
    def payment_request(self):
        return self._payment_request

    @payment_request.setter
    def payment_request(self, value):
        self._payment_request = value