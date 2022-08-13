from typing import Tuple, Any


class Cell:
    is_free = True
    value = 0

    def __bool__(self) -> bool:
        return self.is_free


class TicTacToe:
    """ Tic-tac-toe game field.
    Allows access to fields by [i, j] index,
    also supports [:, j] and [i, :] indexes for GETTING item.
    """

    pole: Tuple[Tuple[Cell, ...], ...]
    POLE_SIZE = 3

    def __init__(self):
        """ Fill with empty cells. """
        self.pole = tuple(
            tuple(Cell() for _ in range(self.POLE_SIZE))
            for _ in range(self.POLE_SIZE)
        )

    def __setitem__(self, key: Tuple[int, int], value: int):
        self._check_index(key)
        self._check_if_cell_is_free(key)
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False

    def __getitem__(self, item: tuple) -> Tuple[int, ...]:
        """ Return item or tuple of items, depending on input index. """
        self._check_index(item, allow_slices=True)
        x, y = item
        if isinstance(x, slice):
            return self._get_column(item[1])
        elif isinstance(y, slice):
            return self._get_row(item[0])

        return self.pole[x][y].value

    def __repr__(self):
        return '\n'.join(
            ' '.join(str(cell.value) for cell in row)
            for row in self.pole
        )

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = 0
                self.pole[i][j].is_free = True

    def _get_row(self, row_index) -> Tuple[int, ...]:
        return tuple(cell.value for cell in self.pole[row_index])

    def _get_column(self, column_index: int) -> Tuple[int, ...]:
        return tuple(row[column_index].value for row in self.pole)

    @classmethod
    def _check_index(cls, index: Any, allow_slices=False):
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError('неверный индекс клетки')

        if (allow_slices
                and any(isinstance(e, slice) for e in index)
                and any(type(e) is int for e in index)):
            cls._check_slice_index(index)
        elif all(type(e) is int for e in index):
            cls._check_single_elem_index(index)  # type: ignore
        else:
            raise IndexError('неверный индекс клетки')

    @classmethod
    def _check_single_elem_index(cls, single_index: Tuple[int, int]):
        if not all(0 <= e <= cls.POLE_SIZE - 1
                   for e in single_index):
            raise IndexError('неверный индекс клетки')

    @classmethod
    def _check_slice_index(cls, slice_index: tuple):
        num, slice_ = slice_index
        if isinstance(num, slice):
            num, slice_ = slice_, num
        if not (0 <= num <= cls.POLE_SIZE - 1
                and slice_ == slice(None, None, None)):
            raise IndexError('неверный индекс клетки')

    def _check_if_cell_is_free(self, index: Tuple[int, int]):
        if not self.pole[index[0]][index[1]]:
            raise ValueError('клетка уже занята')
