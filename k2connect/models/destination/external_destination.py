import abc
from abc import ABC
from dataclasses import dataclass
from typing import Optional

from urlvalidator import ValidationError


@dataclass(kw_only=True)
class ExternalDestination(ABC):
    type: str
    amount: float
    description: str
    nickname: Optional[str] = None
    favourite: Optional[bool] = None

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.type:
            raise ValidationError("Field 'type' must be present.")
        if not self.amount:
            raise ValidationError("Field 'amount' must be present.")
        if not self.description:
            raise ValidationError("Field 'description' must be present.")

    @abc.abstractmethod
    def payload(self) -> dict:
        raise NotImplementedError
