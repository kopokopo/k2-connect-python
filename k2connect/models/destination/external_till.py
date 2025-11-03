from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.destination.external_destination import ExternalDestination


@dataclass
class ExternalTill(ExternalDestination):
    till_number: str

    def validate(self):
        if not self.till_number:
            raise ValidationError("Field 'till_number' must be present.")
        if not self.description:
            raise ValidationError("Field 'description' must be present.")

    def payload(self) -> dict:
        return {
            "type": self.type,
            "nickname": self.nickname,
            "till_number": self.till_number,
            "amount": self.amount,
            "description": self.description,
            "favourite": self.favourite,
        }
