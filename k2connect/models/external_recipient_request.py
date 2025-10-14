from k2connect.models.external_recipient.bank_account import BankAccount
from k2connect.models.external_recipient.external_recipient import ExternalRecipient
from k2connect.models.external_recipient.mobile_wallet import MobileWallet
from k2connect.models.external_recipient.paybill import Paybill
from k2connect.models.external_recipient.till import Till


class ExternalRecipientRequest:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @staticmethod
    def endpoint():
        return "api/v2/pay_recipients"

    def request_body(self):
        return self._build_request().request_body()

    def _build_request(self) -> ExternalRecipient:
        recipient_type = self.kwargs["type"]
        recipient_classes = {
            "mobile_wallet": MobileWallet,
            "bank_account": BankAccount,
            "paybill": Paybill,
            "till": Till,
        }

        if recipient_type not in recipient_classes:
            raise ValueError(f"Undefined recipient type: {recipient_type}")

        return recipient_classes[recipient_type](**self.kwargs)
