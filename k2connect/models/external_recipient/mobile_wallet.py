from dataclasses import dataclass
from typing import Optional

from urlvalidator import ValidationError

from k2connect.models.external_recipient.external_recipient import ExternalRecipient


@dataclass
class MobileWallet(ExternalRecipient):
    first_name: str
    last_name: str
    phone_number: str
    email: Optional[str]
    network: Optional[str]

    def validate(self):
        super().validate()

        if not self.first_name:
            raise ValidationError("Field 'first_name' must be present.")
        if not self.last_name:
            raise ValidationError("Field 'last_name' must be present.")
        if not self.phone_number:
            raise ValidationError("Field 'phone_number' must be present.")

    @staticmethod
    def _validate_phone_number(phone_number: str):
        if len(phone_number) is 12 and not phone_number.startswith("2547"):
            raise ValidationError("Invalid phone number format. Valid phone format: 2547XXXXXXXX")
        if len(phone_number) is 10 and not phone_number.startswith("07"):
            raise ValidationError("Invalid phone number format. Valid phone format: 07XXXXXXXX")

    def payload(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "network": self.network,
        }
