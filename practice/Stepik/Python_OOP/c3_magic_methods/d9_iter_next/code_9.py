from typing import Type, Any, Tuple


class Cell:
    __data: Any

    def __init__(self, data: Any):
        self.data = data

    def __repr__(self):
        return str(self.__data)

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, data: Any):
        self.__data = data


class TableValues:
    _rows: int
    _cols: int
    _type_data: Type
    _cells: Tuple[Tuple[Cell, ...], ...]

    def __init__(self, rows: int, cols: int, type_data: Type = int):
        if not type_data:
            raise ValueError('параметр cell не указан')
        self._rows = rows
        self._cols = cols
        self._type_data = type_data
        self._set_up_cells()

    def __setitem__(self, key: Tuple[int, int], value: Any):
        self._check_index(key)
        self._check_value_type(value)
        self._cells[key[0]][key[1]].data = value

    def __getitem__(self, item: Tuple[int, int]):
        self._check_index(item)
        return self._cells[item[0]][item[1]].data

    def __iter__(self):
        for row in self._cells:
            yield iter(cell.data for cell in row)

    def __repr__(self):
        return str(self._cells)

    def _set_up_cells(self):
        self._cells = tuple(
            tuple(Cell(0) for _ in range(self._cols))
            for _ in range(self._rows)
        )

    def _check_value_type(self, value: Any):
        if type(value) is not self._type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def _check_index(self, index: Any):
        if not (isinstance(index, tuple)
                and all(type(e) is int for e in index)
                and 0 <= index[0] < self._rows
                and 0 <= index[1] < self._cols):
            raise IndexError('неверный индекс')
