from typing import List


class StringValue:
    """ String descriptor for validating strings """

    _min_length: int
    _max_length: int

    def __init__(self, min_length: int = 2, max_length: int = 50):
        self._min_length = min_length
        self._max_length = max_length

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        if (isinstance(value, str)
                and self._min_length <= len(value) <= self._max_length):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class PriceValue:
    """ Price descriptor for validating price """

    _max_value: int

    def __init__(self, max_value: float = 10_000):
        self._max_value = self.transform_price_for_input(max_value)

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and 0 <= value <= self._max_value:
            setattr(instance, self.name, self.transform_price_for_input(value))

    def __get__(self, instance, owner):
        return self.transform_price_for_output(getattr(instance, self.name))

    @staticmethod
    def transform_price_for_input(price: float) -> int:
        return int(price * 100)

    @staticmethod
    def transform_price_for_output(price: int) -> float:
        if price == int(price):
            return int(price / 100)
        return price / 100


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class SuperShop:
    name = StringValue()
    goods = List[Product]

    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        if product not in self.goods:
            self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        if product in self.goods:
            self.goods.remove(product)


if __name__ == '__main__':
    shop = SuperShop("У Балакирева")
    shop.add_product(Product("Курс по Python", 0))
    shop.add_product(Product("Курс по Python ООП", 2000))
    for p in shop.goods:
        print(f"{p.name}: {p.price}")

