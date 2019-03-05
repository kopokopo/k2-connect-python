"""Handles collecting location urls for specific resources in the  headers of responses"""


class ResourceLocation(object):
    def __init__(self, response):
        self.response = response

    def get_location(self):
        resource_location = self.response.headers('Location')
        return resource_location

