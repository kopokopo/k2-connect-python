from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.destination.external_destination import ExternalDestination


@dataclass
class ExternalBankAccount(ExternalDestination):
    account_name: str
    account_number: str
    bank_branch_ref: str

    def validate(self):
        super().validate()

        if not self.account_name:
            raise ValidationError("Field 'account_name' must be present.")
        if not self.account_number:
            raise ValidationError("Field 'account_number' must be present.")
        if not self.bank_branch_ref:
            raise ValidationError("Field 'bank_branch_ref' must be present.")

    def payload(self) -> dict:
        return {
            "type": self.type,
            "nickname": self.nickname,
            "account_name": self.account_name,
            "account_number": self.account_number,
            "bank_branch_ref": self.bank_branch_ref,
            "amount": self.amount,
            "description": self.description,
            "favourite": self.favourite,
        }
