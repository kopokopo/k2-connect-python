from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.transfer_account.transfer_account_request import TransferAccountRequest


@dataclass
class MerchantBankTransferAccount(TransferAccountRequest):
    account_name: str
    account_number: str
    bank_branch_ref: str
    settlement_method: str

    def __post_init__(self):
        self.errors = []
        self.validate()

    def validate(self):
        if not self.account_name:
            self.errors.append("account_name is required.")

        if not self.account_number:
            self.errors.append("account_number is required.")

        if not self.bank_branch_ref:
            self.errors.append("bank_branch_ref is required.")

        if not self.settlement_method:
            self.errors.append("settlement_method is required")

        if self.settlement_method not in ["EFT", "RTS"]:
            self.errors.append("settlement_method must be EFT or RTS")

        if self.errors:
            raise ValidationError(self.errors)

    def request_payload(self):
        return {
            "nickname": self.nickname,
            "account_name": self.account_name,
            "account_number": self.account_number,
            "bank_branch_ref": self.bank_branch_ref,
            "settlement_method": self.settlement_method,
        }

    def endpoint(self):
        return "settlement_bank_account"
