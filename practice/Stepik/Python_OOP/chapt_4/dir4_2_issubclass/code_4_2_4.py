from decimal import Decimal
from typing import Union, Optional, Any, Dict


class Thing:
    name: str
    weight: float
    _price: Decimal

    def __init__(self, name: str, price: float,
                 weight: Union[float, Decimal]):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __eq__(self, other: object):
        if not isinstance(other, Thing):
            return NotImplemented
        return hash(self) == hash(other)

    @property
    def price(self) -> float:
        return float(self._price)

    @price.setter
    def price(self, price: Union[float, Decimal]):
        self._price = Decimal(price)


class DictShop(dict):
    def __init__(self, things: Optional[Dict[Thing, Any]] = None):
        if things:
            self._validate_things(things)
        super().__init__(things or {})

    def __setitem__(self, key: Thing, value: Any):
        self._is_thing(key)
        super().__setitem__(key, value)

    def _validate_things(self, things: Optional[Dict[Thing, Any]]):
        self._check_things_type(things)
        self._check_things_keys(things)

    @staticmethod
    def _check_things_type(things: Optional[Dict[Thing, Any]]):
        if not (isinstance(things, dict) or things is None):
            raise TypeError('аргумент должен быть словарем')

    def _check_things_keys(self, things: Optional[Dict[Thing, Any]]):
        for key in things:
            self._is_thing(key)

    @staticmethod
    def _is_thing(value: Thing):
        if not isinstance(value, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')

