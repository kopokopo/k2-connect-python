"""Handles initializing  k2-connect services"""
from k2client import exceptions
from .requests import Requests


class Service(Requests):
    def __init__(self, client_id, client_secret):

        """
        :param client_id:
        :param client_secret:
        """
        super(Service, self).__init__(client_id, client_secret)

        if client_id or client_secret is None:
            raise exceptions.ValueEmptyError
        elif type(client_id) is not str:
            raise exceptions.InvalidTypeError('')
        elif type(client_secret) is not str:
            raise exceptions.InvalidTypeError('')

        self.client_id = client_id
        self.client_secret = client_secret
        self.production_base_url = 'https://api.kopokopo.com/'
        self.sandbox_base_url = 'https://api-sandbox.kopokopo.com/'

    # TODO: Find out distinctive factor between sandbox and production besides url
    def is_sandbox(self):
        return self.sandbox_base_url

    # build a url
    def make_url(self, url_path):
        if self.is_sandbox():
            return self.sandbox_baseurl + url_path
        else:
            return self.production_baseurl + url_path



