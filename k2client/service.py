"""Handles initializing  k2-connect services"""
from k2client import exceptions
from .requests import Requests
from k2client import validation


class Service(Requests):
    def __init__(self, client_id, client_secret, custom_base_url=None):

        """
        :param client_id: Your application's client ID
        :type client_id: str

        :param client_secret: Your application's client secret (used for Oauth requests)
        :type client_secret : str

        :param custom_base_url: Domain to send requests to if for some reason you want to send your request to something other
                than "https://api.kopokopo.com/oauth/v4/token"
        :type custom_base_url: str
        """
        super(Service, self).__init__(bearer_token=self._bearer_token)

        if client_id is None or client_secret is None:
            raise exceptions.ValueEmptyError
        elif type(client_id) is not str:
            raise exceptions.InvalidTypeError('The client_id: \'' + client_id + '\passed has an invalid type. Ensure it is of type: str')
        elif type(client_secret) is not str:
            raise exceptions.InvalidTypeError('The client_secret: \'' + client_secret + '\passed has an invalid type. Ensure it is of type: str')

        self._client_id = client_id
        self._client_secret = client_secret
        self.production_base_url = 'https://api.kopokopo.com/'
        self.sandbox_base_url = 'https://api-sandbox.kopokopo.com/'
        if custom_base_url is not None:
            if validation.validate_url(custom_base_url) is not False:
                self.custom_base_url = custom_base_url

    # TODO: Find out distinctive factor between sandbox and production besides url
    def is_sandbox(self):
        return self.sandbox_base_url

    def is_production(self):
        return self.production_base_url

    def is_custom_base_url(self):
        return self.custom_base_url

    # build a url
    def build_url(self, url_path):
        """
        :param url_path: Path pointing to the target of a base url
        :type url_path: str
        :return: str
        """
        if self.is_sandbox():
            return self.sandbox_baseurl + url_path
        elif self.is_production():
            return self.production_baseurl + url_path
        elif self.is_custom_base_url():
            return self.custom_base_url + url_path



