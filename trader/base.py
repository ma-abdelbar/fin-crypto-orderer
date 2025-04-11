# trader/base.py

from abc import ABC, abstractmethod

class BaseTrader(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def set_leverage(self, symbol: str, leverage: int):
        pass
