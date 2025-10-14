from dataclasses import dataclass

from urlvalidator import ValidationError


@dataclass
class WebhookSubscriptionRequest:
    event_type: str
    url: str
    scope: str
    scope_reference: str

    def __post_init__(self):
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/webhook_subscriptions"

    def request_payload(self):
        return {
            "event_type": self.event_type,
            "url": self.url,
            "scope": self.scope,
            "scope_reference": self.scope_reference,
        }

    def validate(self):
        if self.event_type is None:
            raise ValueError("event_type is required")

        if self.scope is None:
            raise ValueError("scope is required")

        if self.url is None:
            raise ValueError("url is required")

        if self.event_type not in {"buygoods_transaction_received", "b2b_transaction_received",
                                   "settlement_transfer_completed", "customer_created", "buygoods_transaction_reversed",
                                   "card_transaction_received", "card_transaction_voided", "card_transaction_reversed"
                                   }:
            raise ValidationError("Invalid event type provided.")

        if self.scope not in {"till", "company"}:
            raise ValidationError("Scope must be one of 'till' or 'company'.")

        if self.scope == "till" and not self.scope_reference:
            raise ValidationError("Field 'scope_reference' must be present when scope is 'till'.")
