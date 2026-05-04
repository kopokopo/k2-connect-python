from dataclasses import dataclass, field


@dataclass
class PaymentLinkRequest:
    currency: str
    amount: float
    till_number: str
    payment_reference: str
    note: str
    callback_url: str
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        self.errors = []
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/payment_links"

    def request_body(self):
        return {
            "currency": self.currency,
            "amount": self.amount,
            "till_number": self.till_number,
            "payment_reference": self.payment_reference,
            "note": self.note,
            "metadata": self.metadata,
            "_links": {
                "callback_url": self.callback_url,
            },
        }

    def validate(self):
        if not self.amount:
            raise ValueError("amount is required")

        if not self.currency:
            raise ValueError("currency is required")

        if not self.till_number:
            raise ValueError("till_number is required")

        if not self.callback_url:
            raise ValueError("callback_url is required")
