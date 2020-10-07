from Chair import Chair
from FurnitureFactory import FurnitureFactory
from ModernChair import ModernChair
from ModernTable import ModernTable
from Table import Table


class ModernFurnitureFactory(FurnitureFactory):
    def create_table(self) -> Table:
        print("Modern tale")
        return ModernTable()

    def create_chair(self) -> Chair:
        print("Modern chair")
        return ModernChair()
