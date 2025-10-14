from abc import ABC, abstractmethod
from dataclasses import dataclass

from urlvalidator import ValidationError


@dataclass
class ExternalRecipient(ABC):
    type: str
    nickname: str

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.type:
            raise ValidationError("Field 'type' must be present.")

    def request_body(self):
        return {
            "type": self.type,
            "pay_recipient": self.payload()
        }

    @abstractmethod
    def payload(self):
        raise NotImplementedError
