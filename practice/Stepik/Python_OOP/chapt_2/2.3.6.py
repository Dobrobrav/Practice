from typing import List


class FloatValue:
    """ Descriptor for float values """

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, instance, owner) -> float:
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)


class Cell:
    """ Cell in table """
    value = FloatValue()

    def __init__(self, start_value: float = 0):
        self.value = start_value


class TableSheet:
    """ Table containing cells """
    N: int
    M: int
    cells: List[List[Cell]]

    def __init__(self, N: int, M: int):
        numbers = iter(float(x) for x in range(1, 16))
        self.cells = [[Cell(next(numbers)) for _ in range(M)]
                      for _ in range(N)]


table = TableSheet(N=5, M=3)
