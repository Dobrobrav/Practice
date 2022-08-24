from abc import ABC, abstractmethod
from typing import Union
from decimal import Decimal
from itertools import count

MoneyIn = Union[float, Decimal]


class ShopInterface(ABC):
    @abstractmethod
    def get_id(self) -> int: ...


class ShopItem(ShopInterface):
    __id: int
    _name: str
    _weight: float
    _price: Decimal
    _current_id = count(1)

    def __init__(self, name: str, weight: float, price: MoneyIn):
        self.__id = next(self._current_id)
        self._name = name
        self._weight = weight
        self.price = price  # type: ignore

    @property
    def price(self) -> float:
        return float(self._price)

    @price.setter
    def price(self, price: MoneyIn):
        self._price = Decimal(price)

    def get_id(self) -> int:
        return self.__id
