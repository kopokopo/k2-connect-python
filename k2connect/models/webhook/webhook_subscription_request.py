from dataclasses import dataclass

from urlvalidator import ValidationError

DARAJA_PAYLOAD_SUPPORTED_EVENTS = ["buygoods_transaction_received", "b2b_transaction_received"]

@dataclass
class WebhookSubscriptionRequest:
    event_type: str
    webhook_uri: str
    scope: str
    scope_reference: str
    enable_daraja_payload: bool = False

    def __post_init__(self):
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/webhook_subscriptions"

    def request_payload(self):
        return {
            "event_type": self.event_type,
            "url": self.webhook_uri,
            "scope": self.scope,
            "scope_reference": self.scope_reference,
            "enable_daraja_payload": self.enable_daraja_payload,
        }

    def validate(self):
        if not self.event_type:
            raise ValueError("event_type is required")

        if not self.scope:
            raise ValueError("scope is required")

        if not self.webhook_uri:
            raise ValueError("webhook_uri is required")

        if self.event_type not in {"buygoods_transaction_received", "b2b_transaction_received",
                                   "settlement_transfer_completed", "customer_created", "buygoods_transaction_reversed",
                                   "card_transaction_received", "card_transaction_voided", "card_transaction_reversed"
                                   }:
            raise ValidationError("Invalid event type provided.")

        if self.scope not in {"till", "company"}:
            raise ValidationError("Scope must be one of 'till' or 'company'.")

        if self.scope == "till" and not self.scope_reference:
            raise ValidationError("Field 'scope_reference' must be present when scope is 'till'.")

        if self.enable_daraja_payload and self.event_type not in DARAJA_PAYLOAD_SUPPORTED_EVENTS:
            raise ValidationError(f"Can only enable daraja_payloads for {', '.join(DARAJA_PAYLOAD_SUPPORTED_EVENTS)} webhooks.")
