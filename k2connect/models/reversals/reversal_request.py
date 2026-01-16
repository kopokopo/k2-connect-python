from dataclasses import dataclass, field

from urlvalidator import ValidationError


@dataclass
class ReversalRequest:
    transaction_reference: str
    reason: str
    callback_url: str
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        self.errors = []
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/reversals"

    def request_body(self):
        return {
            "transaction_reference": self.transaction_reference,
            "reason": self.reason,
            "metadata": self.metadata,
            "_links": {
                "callback_url": self.callback_url,
            },
        }

    def validate(self):
        if not self.transaction_reference:
            self.errors.append("transaction_reference is required.")

        if self.reason is None:
            self.errors.append("reason is required.")

        if self.errors:
            raise ValidationError(self.errors)
