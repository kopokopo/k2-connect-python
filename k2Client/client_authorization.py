""" Handles the client authorization using OAuth2.0 Framework """

import requests


class client_authorization(object):
    def __init__(self,
                 client_id=None,
                 client_secret=None,
                 access_url="https://api.kopokopo.com/oauth/v4/token"):
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
        request_body = build_request_body(self.client_id, self.client_secret)
        # make post request
        authorization_request = requests.post(self.access_url, headers, json=request_body)

        return authorization_request

    def access_token(self):
        request = self.request_access()
        request_access_token = request.json().get("access_token")
        return request_access_token


def build_request_body(provided_id, provided_secret):
    req_body = "{\"grant_type\":\"client_credentials\",\"client_id\":" "\"" + provided_id + "\"" ",\"client_secret\":"" \"" + provided_secret + "\"" "}"
    return req_body
