from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.external_recipient.external_recipient import ExternalRecipient


@dataclass
class Paybill(ExternalRecipient):
    paybill_name: str
    paybill_number: str
    paybill_account_number: str

    def validate(self):
        super().validate()

        if not self.paybill_name:
            raise ValidationError("Field 'paybill_name' must be present.")
        if not self.paybill_number:
            raise ValidationError("Field 'paybill_number' must be present.")
        if not self.paybill_account_number:
            raise ValidationError("Field 'paybill_account_number' must be present.")

    def payload(self):
        return {
            "paybill_name": self.paybill_name,
            "paybill_number": self.paybill_number,
            "paybill_account_number": self.paybill_account_number,
            "nickname": self.nickname,
        }
