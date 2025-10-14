from k2connect import service

from k2connect.base_service import BaseService
from k2connect.models.polling.polling_request import PollingRequest


class PollingService(BaseService):
    def __init__(self, base_url, access_token=None):
        super(PollingService, self).__init__(base_url)
        self._access_token = access_token

    def initiate_polling_request(self, kwargs):
        polling_url = self._build_url(PollingRequest.endpoint())

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        polling_request = PollingRequest(**kwargs)
        polling_payload = polling_request.request_payload()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=polling_url,
                                  payload=polling_payload)

    def polling_request_status(self, query_url):
        headers = dict(self._headers)

        return self._query_transaction_status(headers=headers, query_url=query_url)

    @staticmethod
    def polling_request_location(response):
        # ToDO: Gill -  Check this with David
        return service.k2_requests.get_location(response)
