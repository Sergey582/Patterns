from abc import ABC, abstractmethod

from Chair import Chair
from Table import Table


class FurnitureFactory(ABC):
    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_chair(self) -> Chair:
        pass
