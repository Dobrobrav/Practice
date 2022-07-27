class ShopItem:
    """ some comment"""

    _name: str
    _weight: float
    _price: int

    def __init__(self, name: str, weight: float, price: float):
        self._name = name
        self.price = price
        self._weight = weight

    @property
    def price(self) -> float:
        return self._price / 100

    @price.setter
    def price(self, price: float):
        self._price = int(price * 100)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ShopItem):
            return NotImplemented
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(*self.__dict__.values())
