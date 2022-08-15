from typing import Any, Tuple, Dict


class SparseTable:
    _table_map: Dict[Tuple[int, int], 'Cell']
    _cell_quantity_in_rows: Dict[int, int]
    _cell_quantity_in_cols: Dict[int, int]

    def __init__(self):
        self._table_map = {}
        self._cell_quantity_in_rows = {-1: -1}
        self._cell_quantity_in_cols = {-1: -1}

    def __setitem__(self, key: Tuple[int, int], value: Any):
        self.add_data(*key, value)

    def __getitem__(self, item: Tuple[int, int]) -> Any:
        self._check_if_cell_exists_get(*item)
        return self._table_map[item].value

    def __repr__(self):
        return str(self._table_map)

    @property
    def rows(self) -> int:
        return max(self._cell_quantity_in_rows) + 1

    @property
    def cols(self) -> int:
        return max(self._cell_quantity_in_cols) + 1

    def add_data(self, row: int, col: int, data: 'Cell'):
        if (row, col) not in self._table_map:
            self._add_to_rows_and_cols(row, col)
        self._table_map[(row, col)] = Cell(data)

    def remove_data(self, row: int, col: int):
        self._check_if_cell_exists_remove(row, col)
        self._remove_from_rows_and_cols(row, col)
        self._table_map.pop((row, col))

    def _add_to_rows_and_cols(self, row: int, col: int):
        rows = self._cell_quantity_in_rows
        cols = self._cell_quantity_in_cols
        rows[row] = (rows.get(row) + 1) if rows.get(row) else 1  # type: ignore
        cols[col] = (cols.get(col) + 1) if cols.get(col) else 1  # type: ignore

    def _remove_from_rows_and_cols(self, row: int, col: int):
        rows = self._cell_quantity_in_rows
        cols = self._cell_quantity_in_cols
        if rows[row] == 1:
            rows.pop(row)
        else:
            rows[row] -= 1
        if cols[col] == 1:
            cols.pop(col)
        else:
            cols[col] -= 1

    def _check_if_cell_exists_get(self, row: int, col: int):
        if (row, col) not in self._table_map:
            raise ValueError('данные по указанным индексам отсутствуют')

    def _check_if_cell_exists_remove(self, row: int, col: int):
        if (row, col) not in self._table_map:
            raise IndexError('ячейка с указанными индексами не существует')


class Cell:
    value: Any

    def __init__(self, value: Any):
        self.value = value

    def __repr__(self):
        return str(self.value)
