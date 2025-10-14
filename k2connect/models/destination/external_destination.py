import abc
from abc import ABC
from dataclasses import dataclass
from typing import Optional

from urlvalidator import ValidationError


@dataclass
class ExternalDestination(ABC):
    type: str
    amount: float
    description: str
    nickname: Optional[str]
    favourite: Optional[bool]

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.type:
            raise ValidationError("Field 'type' must be present.")
        if self.amount is None:
            raise ValidationError("Field 'amount' must be present.")
        if self.description is None:
            raise ValidationError("Field 'description' must be present.")

    @abc.abstractmethod
    def payload(self) -> dict:
        raise NotImplementedError
