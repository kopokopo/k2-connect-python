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
            "callback_url": self.callback_url,
            "metadata": self.metadata,
        }

    def validate(self):
        if self.amount is None:
            raise ValueError("amount is required")

        if self.till_number is None:
            raise ValueError("till_number is required")

        if self.payment_reference is None:
            raise ValueError("payment_reference is required")

        if self.note is None:
            raise ValueError("note is required")
