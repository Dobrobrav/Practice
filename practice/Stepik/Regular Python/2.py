from typing import List, Union

Number = Union[int, float]


class Product:
    """ Product for shop """

    _current_id = 0
    id: int
    name: str
    weight: Number
    price: Number

    def __init__(self, name: str, weight: Number, price: Number):
        self.__class__._current_id += 1
        self.id = self.__class__._current_id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        # if not isinstance(value, self.__annotations__[key]) or type(value) is bool:
        if type(value) is not self.__annotations__[key] or type(value) is bool:
            raise TypeError("Неверный тип присваиваемых данных.")

        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")


class Shop:
    """ Online shop """

    _name: str
    goods: List[Product]

    def __init__(self, name: str):
        self._name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)


if __name__ == '__main__':
    print(type(5) is Product.__annotations__['weight'])


