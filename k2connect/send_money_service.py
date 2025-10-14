from k2connect import service
from k2connect.base_service import BaseService
from k2connect.models.external_recipient_request import ExternalRecipientRequest
from k2connect.models.send_money_request import SendMoneyRequest


class SendMoneyService(BaseService):

    def __init__(self, base_url, access_token=None):
        super(SendMoneyService, self).__init__(base_url, access_token)
        self._access_token = access_token

    def create_payment(self, kwargs):
        send_money_url = self._build_url(SendMoneyRequest.endpoint())

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        send_money_request = SendMoneyRequest(**kwargs)
        send_money_payload = send_money_request.request_body()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=send_money_url,
                                  payload=send_money_payload)

    def add_external_recipient(self, kwargs):
        add_recipient_url = self._build_url(ExternalRecipientRequest.endpoint())

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        external_recipient_request = ExternalRecipientRequest(**kwargs)
        external_recipient_payload = external_recipient_request.request_body()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=add_recipient_url,
                                  payload=external_recipient_payload)

    @staticmethod
    def send_money_location(response):
        return service.k2_requests.get_location(response)
