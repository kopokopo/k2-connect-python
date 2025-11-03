from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.destination.external_destination import ExternalDestination


@dataclass
class ExternalMpesaWallet(ExternalDestination):
    phone_number: str
    network: str

    def validate(self):
        if self.phone_number.startswith("+"):
            self.phone_number = self.phone_number[1:]

        super().validate()

        if not self.phone_number:
            raise ValidationError("Field 'phone_number' must be present.")
        if not self.description:
            raise ValidationError("Field 'description' must be present.")

        self._validate_phone_number(self.phone_number)

    @staticmethod
    def _validate_phone_number(phone_number: str):
        if len(phone_number) is 12 and not phone_number.startswith("2547"):
            raise ValidationError("Invalid phone number format. Valid phone format: 2547XXXXXXXX")
        if len(phone_number) is 10 and not phone_number.startswith("07"):
            raise ValidationError("Invalid phone number format. Valid phone format: 07XXXXXXXX")

    def payload(self) -> dict:
        return {
            "type": self.type,
            "nickname": self.nickname,
            "phone_number": self.phone_number,
            "network": self.network,
            "amount": self.amount,
            "description": self.description,
            "favourite": self.favourite,
        }
