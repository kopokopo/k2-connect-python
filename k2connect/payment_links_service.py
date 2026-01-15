from k2connect import service
from k2connect.base_service import BaseService
from k2connect.models.payment_links.payment_link_request import PaymentLinkRequest


class PaymentLinksService(BaseService):

    def __init__(self, base_url, access_token=None):
        super(PaymentLinksService, self).__init__(base_url, access_token)
        self._access_token = access_token

    def create_payment_link(self, kwargs):
        payment_links_url = self._build_url(PaymentLinkRequest.endpoint())

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        payment_link_request = PaymentLinkRequest(**kwargs)
        payment_link_payload = payment_link_request.request_body()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=payment_links_url,
                                  payload=payment_link_payload)

    def fetch_payment_link(self, kwargs):
        fetch_payment_link_url = (
            "{}/{}".format(self._build_url(PaymentLinkRequest.endpoint()), kwargs["payment-link-reference"]))
        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        return self._send_request(headers=headers,
                                  method='GET',
                                  url=fetch_payment_link_url)

    def cancel_payment_link(self, kwargs):
        cancel_payment_links_url = (
            "{}/{}/cancel".format(self._build_url(PaymentLinkRequest.endpoint()), kwargs["payment-link-reference"]))

        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        return self._send_request(headers=headers,
                                  method='POST',
                                  url=cancel_payment_links_url)

    @staticmethod
    def payment_link_location(response):
        return service.k2_requests.get_location(response)
