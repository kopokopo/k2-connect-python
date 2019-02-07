""" Handles the client authorization using OAuth2.0 Framework """

import requests
import os

default_url = os.getenv('DEFAULT_OAUTH_URL')


class ClientAuthorization(object):
    def __init__(self,
                 client_id=None,
                 client_secret=None,
                 access_url=default_url):
        """
        :param client_id: Your application's client ID
        :type client_id: str

        :param client_secret: Your application's client secret (used for Oauth requests)
        :type client_secret : str

        :param access_url: Domain to send requests to if for some reason you want to send your request to something other
                than "https://api.kopokopo.com/oauth/v4/token"
        :type access_url: str

        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_url = access_url

    def request_access(self):
        # set headers
        headers = {'content-type': "application/x-www-form-urlencoded"}
        # set request body
        payload = {self.client_id, self.client_secret}
        # make post request
        authorization_response = requests.post(self.access_url, headers, payload)

        return authorization_response


def access_token(response):
    response_access_token = response.json().get('access_token')
    return response_access_token


def token_expiry_time(response):
    response_expiry_time = response.json().get('expires_in')
    return response_expiry_time



