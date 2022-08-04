from typing import Type, Any


class Float:
    _value = 0.0

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        if not isinstance(value, float):
            raise ValueError('должно быть целое число')  # should be TypeError!
        self._value = value


class Integer:
    _value = 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        if type(value) is not int:
            raise ValueError('должно быть целое число')
        self._value = value


class Array:
    max_length: int
    cell: Type
    _elements: list

    def __init__(self, max_length: int, cell: Type):
        self.max_length = max_length
        self.cell = cell
        self._elements = [cell() for _ in range(max_length)]

    def __setitem__(self, key: int, value: Any):
        self._check_index(key)
        self._elements[key].value = value

    def __getitem__(self, item: int) -> Any:
        self._check_index(item)
        return self._elements[item].value

    def __str__(self):
        return ' '.join(str(e.value) for e in self._elements)

    def _check_index(self, index: int):
        if not (type(index) is int and 0 <= index <= self.max_length - 1):
            raise IndexError('неверный индекс для доступа к элементам массива')
