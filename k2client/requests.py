"""Handles requests for the library"""
import os
import requests
from k2client import exceptions
from k2client import validation


class Requests(object):

    def __init__(self, bearer_token):
        """
        :param bearer_token: Access token to be used to make calls to the Kopo Kopo API
        :type  bearer_token: str
        """
        self._bearer_token = bearer_token
        self._headers = {
            'Accept': 'application/vnd.kopokopo.v4.hal + json',
            'Content-Type': 'application/vnd.kopokopo.v4.hal + json',
            'Authorization': 'Bearer\'' + self._bearer_token + '\''
        }

    @staticmethod
    def __get_request(url, headers, params):
        """
        :param url: URL to which GET request is performed
        :param headers: Headers to be sent for a GET request
        :param params: Query parameters for a GET request
        :return: Http response object
        """
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
        )

        return response

    @staticmethod
    def __post_request(url, headers, payload, params):
        """
        :param url: URL to which POST request is performed
        :param headers: Headers to be sent for a POST request
        :param payload: Payload to be sent for a POST request
        :param params: Query parameters for a POST request
        :return: Http response object
        """
        response = requests.post(
            url=url,
            headers=headers,
            params=params,
            payload=payload,
        )
        return response

    def make_requests(self, headers, method, url, payload=None, params=None):
        """
        :param headers: Headers to be sent for a HTTP request
        :param method: Method of the HTTP request
        :param url: URL to which HTTP request is performed
        :param payload: Payload to be sent for a HTTP request
        :param params: Query parameters for a HTTP request
        :return: HTTP response object
        """
        method = method.upper
        try:
            if validation.validate_url(url) is True:
                # check method type
                if method == 'GET':
                    response = self.__get_request(url=url, headers=headers, params=params)
                elif method == 'POST':
                    response = self.__post_request(url=url, headers=headers, payload=payload, params=params)
                else:
                    raise exceptions.InvalidRequestMethodError('The method passed is not recognized by k2-connect')

                # define status code
                status_code = response.status_code

                if 200 <= status_code <= 300:
                    response_payload = response.json()
                    return response_payload
                else:
                    return response.reason

        except exceptions.InsecureURLError:
            raise exceptions.InsecureURLError('Invalid URL')

