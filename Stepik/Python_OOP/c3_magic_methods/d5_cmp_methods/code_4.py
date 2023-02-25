class Dimensions:
    """ Class that represents dimensions of items;
     class contains a, b, c (x, y, z) dimensions in range [10; 10_000]
     and can calculate volume. """

    MIN_DIMENSION = 10
    MAX_DIMENSION = 10_000
    __a: float
    __b: float
    __c: float

    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return self.volume >= other.volume

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Dimensions):
            return NotImplemented
        return self.volume > other.volume

    @property
    def volume(self) -> float:
        return self.a * self.b * self.c

    @classmethod
    def _check_value(cls, value: float) -> bool:
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float) -> None:
        if self._check_value(a):
            self.__a = a

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float) -> None:
        if self._check_value(b):
            self.__b = b

    @property
    def c(self) -> float:
        return self.__c

    @c.setter
    def c(self, c: float) -> None:
        if self._check_value(c):
            self.__c = c


class ShopItem:
    """ Class that represents items of shop;
     class contains name, price and dimensions of item. """

    name: str
    dim: Dimensions
    _price: int

    def __init__(self, name: str, price: float, dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim

    @property
    def price(self) -> float:
        return self.price / 100

    @price.setter
    def price(self, price: float) -> None:
        self._price = int(price * 100)


if __name__ == '__main__':
    lst_shop = [
        ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
        ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
        ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
        ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200)),
    ]

    lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim)
