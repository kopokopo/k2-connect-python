""" Handles the client authorization using OAuth2.0 Framework """
import requests
from urllib.parse import urlencode
from .requests import Requests
from .service import Service


# for sandbox:
# https://api-sandbox.kopokopo.com/oauth/v4/token
# for production:
# https://api.kopokopo.com/oauth/v4/token

url_path = 'oauth/v4/token'


class AuthorizationService(Service):
    def __init__(self, client_id, client_secret):

        """
        :param client_id: Your application's client ID
        :type client_id: str

        :param client_secret: Your application's client secret (used for Oauth requests)
        :type client_secret : str

        """
        super(AuthorizationService, self).__init__(client_id, client_secret)
        self.client_id = client_id
        self.client_secret = client_secret

    def request_access(self):
        # define url
        url = self.make_url(url_path)

        # define custom headers
        headers = dict(self._headers)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers.__delitem__('Authorization')

        # define payload
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant-type': 'client-credentials'}

        # url-encode payload
        url = url.format(urlencode(payload))

        # define response
        response = self.make_requests(headers=headers, method='POST', url=url)

        return response


def access_token(response):
    response_access_token = response.json().get('access_token')
    return response_access_token


def token_expiry_time(response):
    response_expiry_time = response.json().get('expires_in')
    return response_expiry_time



