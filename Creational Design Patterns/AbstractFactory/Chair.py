from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def get_price(self):
        pass
