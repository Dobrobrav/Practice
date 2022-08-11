from typing import Type, Any
from random import randint

PoleTable = tuple[tuple['Cell', ...], ...]


class Cell:
    """ Cell in GamePole. """

    __is_mine = False
    __number: int
    __is_open = False

    def __bool__(self):
        return not self.is_open

    def __repr__(self):
        # if not hasattr(self, 'number'):
        #     return 'Nah'

        # closed_or_open = 'open' if self.is_open else 'closed'
        mine_or_clear = 'mine' if self.is_mine else 'clear'
        # return f"{closed_or_open}, mines around: {self.number}, {mine_or_clear}"
        return mine_or_clear

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        self._validate_bool(is_mine)
        self.__is_mine = is_mine

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, mines_around: int):
        self._validate_mines_around_number(mines_around)
        self.__number = mines_around

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open: bool):
        self._validate_bool(is_open)
        self.__is_open = is_open

    @staticmethod
    def _validate_bool(value: Any):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")

    @staticmethod
    def _validate_mines_around_number(value: Any):
        if type(value) is not int or not 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")


class MetaSingleton(type):
    """ Singleton metaclass. """

    _instances: dict[Type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class GamePole(metaclass=MetaSingleton):
    """ Sapper game field. """

    N: int
    M: int
    total_mines: int
    __pole_cells: PoleTable

    def __init__(self, N: int, M: int, total_mines: int):
        self.N = N
        self.M = M
        self.total_mines = total_mines

    def __repr__(self):
        return f"N: {self.N}, M: {self.M}, mines: {self.total_mines}"

    def init_pole(self):
        """ Set up all mines and set all cells closed. """
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.M))
                                  for _ in range(self.N))

        # setting up mines
        mines_to_set_up = self.total_mines
        while mines_to_set_up > 0:
            cell_to_mine = self.pole[randint(0, self.N - 1)][randint(0, self.M - 1)]
            if cell_to_mine.is_mine:
                continue

            cell_to_mine.is_mine = True
            mines_to_set_up -= 1

        # counting mines around
        for i, row in enumerate(self.pole):
            for j, cell in enumerate(row):
                if not cell.is_mine:
                    cell.number = self._count_mines_around(i, j)

    def open_cell(self, i: int, j: int):
        self._check_indexes(i, j)
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(' '.join('*' if cell.is_mine else str(cell.number) for cell in row))

    def _check_indexes(self, i: int, j: int):
        if {type(i), type(j)} != {int} or self.N <= i or self.M <= j:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def _count_mines_around(self, i: int, j: int) -> int:
        # creating a frame of clear mines around the field
        wrapped_pole = (
                [[Cell()] * (len(self.pole) + 2)]
                + [[Cell()] + list(row) + [Cell()] for row in self.pole]
                + [[Cell()] * (len(self.pole) + 2)]
        )
        i, j = i + 1, j + 1

        return sum(
            cell.is_mine for row in wrapped_pole[i - 1: i + 2]
            for cell in row[j - 1: j + 2]
        )

    @property
    def pole(self) -> PoleTable:
        return self.__pole_cells
