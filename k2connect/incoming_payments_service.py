from k2connect.base_service import BaseService
from k2connect.models.incoming_payments.incoming_payment_request import IncomingPaymentRequest


class IncomingPaymentsService(BaseService):
    def __init__(self, base_url, access_token):
        super(IncomingPaymentsService, self).__init__(base_url)
        self._access_token = access_token

    def create_incoming_payment(self, kwargs):
        headers = dict(self._headers)

        incoming_payment_request = IncomingPaymentRequest(**kwargs)
        incoming_payment_url = self._build_url(IncomingPaymentRequest.endpoint())
        incoming_payment_request_payload = incoming_payment_request.request_payload()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=incoming_payment_url,
                                  payload=incoming_payment_request_payload)

    def view_incoming_payment(self, kwargs):
        headers = dict(self._headers)

        incoming_payment_url = "{}/{}".format(self._build_url(IncomingPaymentRequest.endpoint()),
                                              kwargs["incoming_payment_reference"])
        return self._send_request(headers=headers,
                                  method='GET',
                                  url=incoming_payment_url)
