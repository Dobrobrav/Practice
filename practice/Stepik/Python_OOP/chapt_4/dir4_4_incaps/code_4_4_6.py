class Furniture:
    _name: str
    _weight: float

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self.__verify_name(name)
        self._name = name

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self.__verify_weight(weight)
        self._weight = weight

    @staticmethod
    def __verify_name(name: str):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight: float):
        if not (type(weight) in (float, int) and weight > 0):
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self) -> tuple:
        return tuple(value for attr, value in self.__dict__.items()
                     if attr.startswith("_") and attr[-1] != '__')


class Closet(Furniture):
    _tp: bool
    _doors: int

    def __init__(self, name: str, weight: float, tp: bool, doors: int):
        super(Closet, self).__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    _height: float

    def __init__(self, name: str, weight: float, height: float):
        super(Chair, self).__init__(name, weight)
        self._height = height


class Table(Furniture):
    _height: float
    _square: float

    def __init__(self, name: str, weight: float,
                 height: float, square: float):
        super(Table, self).__init__(name, weight)
        self._height = height
        self._square = square
