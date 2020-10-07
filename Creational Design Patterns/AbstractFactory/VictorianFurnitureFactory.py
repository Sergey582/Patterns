from Chair import Chair
from FurnitureFactory import FurnitureFactory
from Table import Table
from VictorianChair import VictorianChair
from VictorianTable import VictorianTable


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        print("Victorian chair")
        return VictorianChair()

    def create_table(self) -> Table:
        print("Victorian table")
        return VictorianTable()
