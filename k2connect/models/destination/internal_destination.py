from abc import abstractmethod, ABC
from dataclasses import dataclass

from urlvalidator import ValidationError


@dataclass
class InternalDestination(ABC):
    type: str
    amount: float

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.type:
            raise ValidationError("Field 'type' must be present.")
        if self.amount is None:
            raise ValidationError("Field 'amount' must be present.")

    @abstractmethod
    def payload(self) -> dict:
        raise NotImplementedError
