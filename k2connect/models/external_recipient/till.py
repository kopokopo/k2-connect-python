from dataclasses import dataclass

from urlvalidator import ValidationError

from k2connect.models.external_recipient.external_recipient import ExternalRecipient


@dataclass
class Till(ExternalRecipient):
    till_name: str
    till_number: str

    def validate(self):
        super().validate()

        if not self.till_name:
            raise ValidationError("Field 'till_name' must be present.")
        if not self.till_number:
            raise ValidationError("Field 'till_number' must be present.")

    def payload(self):
        return {
            "till_name": self.till_name,
            "till_number": self.till_number,
            "nickname": self.nickname,
        }
