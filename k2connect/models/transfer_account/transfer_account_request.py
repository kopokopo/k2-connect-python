from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class TransferAccountRequest(ABC):
    type: str
    nickname: Optional[str] = None

    @abstractmethod
    def request_payload(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def endpoint(self):
        raise NotImplementedError
