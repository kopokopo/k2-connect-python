from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.transfer_account.transfer_account_request import TransferAccountRequest


@dataclass
class MerchantMpesaTransferAccount(TransferAccountRequest):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    network: str

    def __post_init__(self):
        self.errors = []
        self.validate()

    def validate(self):
        if not self.first_name:
            self.errors.append("first_name is required.")

        if not self.last_name:
            self.errors.append("last_name is required.")

        if not self.phone_number:
            self.errors.append("phone_number is required.")

        if self.errors:
            raise ValidationError(self.errors)

    def request_payload(self):
        return {
            "nickname": self.nickname,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "network": self.network,
        }

    def endpoint(self):
        return "settlement_merchant_wallet"
