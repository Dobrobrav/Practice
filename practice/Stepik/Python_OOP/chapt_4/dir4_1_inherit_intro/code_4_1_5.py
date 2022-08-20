from decimal import Decimal
from typing import Union, Optional, Tuple
from itertools import count


class Thing:
    id: int
    name: str
    weight: Optional[float] = None
    dims: Optional[Tuple[float, float, float]] = None
    memory: Optional[int] = None
    frm: Optional[str] = None
    _things_id = count(1)
    _price: Decimal

    def __init__(self, name: str, price: Union[float, str, Decimal]):
        self.id = next(self._things_id)
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return float(self._price)

    @price.setter
    def price(self, price: float):
        self._price = Decimal(price)

    def get_data(self) -> tuple:
        return tuple(
            getattr(self, attr_name)
            for attr_name in ('id', 'name', 'price', 'weight',
                              'dims', 'memory', 'frm')
        )


class Table(Thing):
    def __init__(self, name: str, price: float, weight: float,
                 dims: Tuple[float, float, float]):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name: str, price: float, memory: int, frm: str):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


if __name__ == '__main__':
    table = Table("Круглый", 1024, 812.55, (700, 750, 700))
    book = ElBook("Python ООП", 2000, 2048, 'pdf')
    print(*table.get_data())
    print(*book.get_data())
