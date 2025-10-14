from urllib.parse import urlparse

import requests

from k2connect import exceptions
from k2connect import validation


class K2Requests:
    def __init__(self, access_token=None):
        self._headers = {
            'Accept': 'application/vnd.kopokopo.v4.hal+json',
            'Content-Type': 'application/json',
            'User-Agent': 'Kopokopo-Python-SDK',
            'Authorization': f"Bearer #{access_token}"
        }

    @staticmethod
    def __get_request(headers, params, url):
        response = requests.get(
            headers=headers,
            params=params,
            url=url)
        return response

    @staticmethod
    def __post_request(headers, url, payload, data):

        response = requests.post(
            headers=headers,
            json=payload,
            data=data,
            url=url,
        )

        return response

    def _send_request(self,
                      headers,
                      method,
                      url,
                      data=None,
                      payload=None,
                      params=None):

        if validation.validate_url(url) is True:
            if method == 'GET':
                response = self.__get_request(url=url,
                                              headers=headers,
                                              params=params)
            elif method == 'POST':
                response = self.__post_request(url=url,
                                               headers=headers,
                                               payload=payload,
                                               data=data)
            else:
                raise exceptions.InvalidArgumentError('Method not recognized by k2-connect')

            status_code = response.status_code

            if 200 <= status_code <= 300:
                if urlparse(url).path == '/oauth/token' or method == 'GET':
                    return response.json()
                response_location = response.headers.get('location')
                return response_location
            response_error = {
                'error_code': status_code,
                'error_content': response.text
            }
            raise exceptions.K2Error(response_error)
        return exceptions.K2Error

    def _query_transaction_status(self,
                                  headers,
                                  query_url):

        validation.validate_url(query_url)

        return self._send_request(url=query_url,
                                  method='GET',
                                  headers=headers)


def get_location(response):
    resource_location = response.headers('location')
    return resource_location
