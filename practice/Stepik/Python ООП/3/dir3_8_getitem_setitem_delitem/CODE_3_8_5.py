from typing import Type, Any


class StringValue:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        if type(value) is not str:
            raise ValueError('возможны только строковые значения')  # must be TypeError!
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        if type(value) is not int:
            raise ValueError('возможны только целочисленные значения')  # must be TypeError!
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

    def __repr__(self):
        return str(self.value)


class CellString:
    value = StringValue()

    def __init__(self, start_value=' '):
        self.value = start_value

    def __repr__(self):
        return self.value


class TableValues:
    _rows: int
    _cols: int
    _cell: Type
    cells: tuple[tuple, ...]

    def __init__(self, rows: int, cols: int, cell: Type = None):
        if not cell:
            raise ValueError('параметр cell не указан')
        self._rows = rows
        self._cols = cols
        self._cell = cell

        self.cells = tuple(
            tuple(self._cell() for _ in range(self._cols))
            for _ in range(self._rows)
        )

    def __setitem__(self, key: tuple[int, int], value: Any):
        self.cells[key[0]][key[1]].value = value

    def __getitem__(self, item: tuple[int, int]):
        return self.cells[item[0]][item[1]].value

    def __repr__(self):
        return str(self.cells)
