from dataclasses import dataclass
from datetime import datetime

from urlvalidator import ValidationError


@dataclass
class PollingRequest:
    from_time: datetime
    to_time: datetime
    callback_url: str
    scope: str
    scope_reference: str

    def __post_init__(self):
        self.errors = []
        self.validate()

    @staticmethod
    def endpoint():
        return "api/v2/polling"

    def request_payload(self):
        return {
            "scope": self.scope,
            "scope_reference": self.scope_reference,
            "from_time": self.from_time,
            "to_time": self.to_time,
            "_links": {
                "callback_url": self.callback_url,
            },
        }

    def validate(self):
        if self.from_time is None:
            raise ValueError("from_time is required")

        if self.to_time is None:
            raise ValueError("to_time is required")

        if self.callback_url is None:
            raise ValueError("callback_url is required")

        if self.scope is None:
            raise ValueError("scope is required")

        if self.scope not in {"till", "company"}:
            raise ValidationError("Scope must be one of 'till' or 'company'.")

        if self.scope == "till" and not self.scope_reference:
            raise ValidationError("Field 'scope_reference' must be present when scope is 'till'.")
