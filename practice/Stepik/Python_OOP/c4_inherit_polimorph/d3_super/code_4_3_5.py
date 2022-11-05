from decimal import Decimal
from typing import Union, List

MoneyIn = Union[float, Decimal]


class SellItem:
    name: str
    _price: Decimal

    def __init__(self, name: str, price: MoneyIn):
        self.name = name
        self.price = price

    @property
    def price(self):
        return float(self._price)

    @price.setter
    def price(self, price: MoneyIn):
        self._price = Decimal(price)


class House(SellItem):
    material: str
    square: float

    def __init__(self, name: str, price: MoneyIn,
                 material: str, square: float):
        super(House, self).__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    size: float
    rooms: int

    def __init__(self, name: str, price: MoneyIn,
                 size: float, rooms: int):
        super(Flat, self).__init__(name, price)
        self.size = size
        self.rooms = rooms
        
        
class Land(SellItem):
    square: float
    
    def __init__(self, name: str, price: MoneyIn, square: float):
        super(Land, self).__init__(name, price)
        self.square = square


class Agency:
    name: str
    _sell_items: List[SellItem]

    def __init__(self, name: str):
        self.name = name
        self._sell_items = []

    def add_object(self, obj: SellItem):
        self._sell_items.append(obj)

    def remove_object(self, obj: SellItem):
        self._sell_items.remove(obj)

    def get_objects(self) -> List[SellItem]:
        return self._sell_items

        
