from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.destination.internal_destination import InternalDestination


@dataclass
class MerchantMpesaWallet(InternalDestination):
    reference: str

    def validate(self):
        super().validate()

        if not self.reference:
            raise ValidationError("Field 'reference' must be present.")

    def payload(self) -> dict:
        return {
            "type": self.type,
            "reference": self.reference,
            "amount": self.amount,
        }
