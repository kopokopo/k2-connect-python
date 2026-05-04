from dataclasses import dataclass, field

from urlvalidator import ValidationError

from k2connect.models.destination.external_bank_account import ExternalBankAccount
from k2connect.models.destination.external_mpesa_wallet import ExternalMpesaWallet
from k2connect.models.destination.external_paybill import ExternalPaybill
from k2connect.models.destination.external_till import ExternalTill
from k2connect.models.destination.merchant_bank_account import MerchantBankAccount
from k2connect.models.destination.merchant_mpesa_wallet import MerchantMpesaWallet


@dataclass
class SendMoneyRequest:
    source_identifier: str
    destinations: list
    callback_url: str
    currency: str
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        self.errors = []
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/send_money"

    def request_body(self):
        return {
            "source_identifier": self.source_identifier,
            "destinations": self._build_destination_requests(self.destinations),
            "currency": "KES",
            "metadata": self.metadata,
            "_links": {
                "callback_url": self.callback_url,
            },
        }

    def _build_destination_requests(self, destinations):
        if not destinations:
            return []
        return [self._build_destination_request(d).payload() for d in destinations]

    def _build_destination_request(self, destination):
        destination_type = destination.get("type")

        destination_classes = {
            "mobile_wallet": ExternalMpesaWallet,
            "bank_account": ExternalBankAccount,
            "paybill": ExternalPaybill,
            "till": ExternalTill,
            "merchant_bank_account": MerchantBankAccount,
            "merchant_wallet": MerchantMpesaWallet,
        }

        if destination_type not in destination_classes:
            raise ValueError(f"Undefined destination type: {destination_type}")

        return destination_classes[destination_type](**destination)

    def validate(self):

        if not self.callback_url:
            self.errors.append("callback_url is required.")

        if self.currency is not None and self.currency != "KES":
            self.errors.append("currency must be 'KES'.")

        if self.errors:
            raise ValidationError(self.errors)
