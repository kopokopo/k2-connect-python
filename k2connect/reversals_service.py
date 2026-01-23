from k2connect import service
from k2connect.base_service import BaseService
from k2connect.models.reversals.reversal_request import ReversalRequest


class ReversalsService(BaseService):

    def __init__(self, base_url, access_token=None):
        super(ReversalsService, self).__init__(base_url, access_token)
        self._access_token = access_token

    def initiate_reversal(self, kwargs):
        reversal_url = self._build_url(ReversalRequest.endpoint())

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        reversal_request = ReversalRequest(**kwargs)
        reversal_payload = reversal_request.request_body()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=reversal_url,
                                  payload=reversal_payload)

    def get_status(self, kwargs):
        fetch_reversal_url = (
            "{}/{}".format(self._build_url(ReversalRequest.endpoint()), kwargs['reversal-reference']))

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        return self._send_request(headers=headers,
                                  method='GET',
                                  url=fetch_reversal_url)

    @staticmethod
    def reversal_location(response):
        return service.k2_requests.get_location(response)
