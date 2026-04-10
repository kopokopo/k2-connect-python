from k2connect.base_service import BaseService
from k2connect.models.stk_push.stk_push_request import StkPushRequest


class StkPushService(BaseService):

    def __init__(self, base_url, access_token=None):
        super(StkPushService, self).__init__(base_url)
        self._access_token = access_token

    def initiate_request(self, kwargs):
        incoming_payments_url = self._build_url(StkPushRequest.endpoint())

        headers = dict(self._headers)

        stk_push_request = StkPushRequest(**kwargs)
        stk_push_request_payload = stk_push_request.request_body()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=incoming_payments_url,
                                  payload=stk_push_request_payload)
