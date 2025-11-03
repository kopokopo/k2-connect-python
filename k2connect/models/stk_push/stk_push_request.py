from dataclasses import dataclass, field

from urlvalidator import ValidationError


@dataclass
class StkPushRequest:
    till_number: str
    payment_channel: list
    first_name: str
    middle_name: str
    last_name: str
    phone_number: str
    email: str
    amount: float
    callback_url: str
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        self.errors = []
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/incoming_payments"

    def request_body(self):
        return {
            "payment_channel": self.payment_channel,
            "till_number": self.till_number,
            "subscriber": {
                "first_name": self.first_name,
                "middle_name": self.middle_name,
                "last_name": self.last_name,
                "phone_number": self.phone_number,
                "email": self.email,
            },
            "amount": {
                "currency": "KES",
                "value": self.amount,
            },
            "metadata": self.metadata,
            "_links": {
                "callback_url": self.callback_url,
            },
        }

    def validate(self):
        if not self.callback_url:
            self.errors.append("till_number is required.")

        if not self.phone_number:
            self.errors.append("phone_number is required.")

        if not self.amount:
            self.errors.append("amount is required.")

        if not self.callback_url:
            self.errors.append("callback_url is required.")

        if self.errors:
            raise ValidationError(self.errors)

        self._validate_phone_number(self.phone_number)

    @staticmethod
    def _validate_phone_number(phone_number: str):
        if len(phone_number) is 12 and not phone_number.startswith("2547"):
            raise ValidationError("Invalid phone number format. Valid phone format: 2547XXXXXXXX")
        if len(phone_number) is 10 and not phone_number.startswith("07"):
            raise ValidationError("Invalid phone number format. Valid phone format: 07XXXXXXXX")
