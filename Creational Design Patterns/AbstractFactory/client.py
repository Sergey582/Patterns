from FurnitureFactory import FurnitureFactory
from ModernFurnitureFactory import ModernFurnitureFactory
from VictorianFurnitureFactory import VictorianFurnitureFactory


def get_furniture_price(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    price = chair.get_price() + table.get_price()
    return price


factory = VictorianFurnitureFactory()
print(get_furniture_price(factory))
factory = ModernFurnitureFactory()
print(get_furniture_price(factory))
