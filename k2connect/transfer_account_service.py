from k2connect.base_service import BaseService
from k2connect.models.transfer_account.merchant_bank_transfer_account import MerchantBankTransferAccount
from k2connect.models.transfer_account.merchant_mpesa_transfer_account import MerchantMpesaTransferAccount


class TransferAccountService(BaseService):
    def __init__(self, base_url, access_token):
        super(TransferAccountService, self).__init__(base_url)
        self._access_token = access_token

    def add_transfer_account(self, kwargs):
        headers = dict(self._headers)

        if self._access_token:
            headers['Authorization'] = f"Bearer {self._access_token}"

        transfer_account_request = self._build_transfer_account_request(**kwargs)
        transfer_url = self._build_url(transfer_account_request.endpoint())
        transfer_account_request_payload = transfer_account_request.request_payload()
        return self._send_request(headers=headers,
                                  method='POST',
                                  url=transfer_url,
                                  payload=transfer_account_request_payload)

    def _build_transfer_account_request(self, request):
        request_type = request.get("type")

        request_classes = {
            "merchant_bank_account": MerchantBankTransferAccount,
            "merchant_wallet": MerchantMpesaTransferAccount,
        }

        if request_type not in request_classes:
            raise ValueError(f"Unknown transfer account type: {request_type}")

        return request_classes[request_type](**request)
