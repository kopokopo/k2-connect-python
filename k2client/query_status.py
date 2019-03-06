"""Handles sending a query to get payment status"""
from k2client.requests import Requests


class QueryStatus(Requests):
    def __init__(self, bearer_token):
        """
        :param bearer_token: Access token to be used to make calls to the Kopo Kopo API
        :type bearer_token: str
        """
        self._bearer_token = bearer_token
        super(QueryStatus, self).__init__(bearer_token=self._bearer_token)

    def query_transaction_status(self, url):
        """
        :param url: URL to which query is made
        :return: Http response object
        """
        query_response = self.make_requests(url=url, method='GET', headers=self._headers)
        return query_response

