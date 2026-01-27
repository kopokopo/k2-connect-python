from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Subscriber:
    first_name: str
    last_name: str
    phone_number: str
    middle_name: Optional[str] = None
    email: Optional[str] = None


@dataclass(frozen=True)
class Amount:
    currency: str
    value: float


@dataclass
class IncomingPaymentRequest:
    payment_channel: str
    till_number: str
    subscriber: Subscriber
    callback_url: str
    amount: Amount
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        self.errors = []
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/incoming_payments"

    def request_payload(self):
        return {
            "payment_channel": self.payment_channel,
            "till_number": self.till_number,
            "subscriber": self.subscriber.__dict__,
            "metadata": self.metadata,
            "amount": self.amount.__dict__,
            "_links": {
                "callback_url": self.callback_url,
            },
        }

    def validate(self):
        if not self.amount:
            raise ValueError("amount is required")

        if not self.till_number:
            raise ValueError("till_number is required")

        if not self.subscriber.phone_number:
            raise ValueError("subscriber phone_number is required")

        if not self.callback_url:
            raise ValueError("callback_url is required")
