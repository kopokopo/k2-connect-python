from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.destination.external_destination import ExternalDestination


@dataclass
class ExternalPaybill(ExternalDestination):
    paybill_number: str
    paybill_account_number: str

    def validate(self):
        super().validate()

        if not self.paybill_number:
            raise ValidationError("Field 'paybill_number' must be present.")
        if not self.description:
            raise ValidationError("Field 'description' must be present.")
        if not self.paybill_account_number:
            raise ValidationError("Field 'paybill_account_number' must be present.")

    def payload(self) -> dict:
        return {
            "type": self.type,
            "nickname": self.nickname,
            "paybill_number": self.paybill_number,
            "paybill_account_number": self.paybill_account_number,
            "amount": self.amount,
            "description": self.description,
            "favourite": self.favourite,
        }
