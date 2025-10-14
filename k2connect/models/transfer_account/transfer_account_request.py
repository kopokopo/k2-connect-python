from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class TransferAccountRequest(ABC):
    type: str
    nickname: str

    @abstractmethod
    def request_payload(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def endpoint(self):
        raise NotImplementedError
