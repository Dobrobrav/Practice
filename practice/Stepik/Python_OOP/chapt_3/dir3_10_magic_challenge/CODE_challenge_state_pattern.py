from typing import Tuple, Any, Dict
from abc import ABC, abstractmethod
from enum import Enum


class GameState(Enum):
    NOT_STARTED = 0
    COMPUTER_TURN = 1
    HUMAN_TURN = 2
    COMPUTER_WIN = 3
    HUMAN_WIN = 4
    DRAW = 5


class IGameState(ABC):
    @property
    @abstractmethod
    def is_human_win(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_computer_win(self) -> bool:
        ...

    @property
    @abstractmethod
    def is_draw(self) -> bool:
        ...

    @abstractmethod
    def human_go(self, game: 'TicTacToe'):
        ...

    @abstractmethod
    def computer_go(self, game: 'TicTacToe'):
        ...


class NotStarted(IGameState):
    @property
    def is_human_win(self) -> False:
        return False

    @property
    def is_computer_win(self) -> False:
        return False

    @property
    def is_draw(self) -> False:
        return False

    def human_go(self, game: 'TicTacToe'):
        self.make_human_move(game)
        winner = self._get_winner(game)
        # it's bucking complicated. Need to consider all the options
        # if winner
        # game.state

    def computer_go(self, game: 'TicTacToe'):
        pass


class ComputerTurn(IGameState):
    @property
    def is_human_win(self) -> False:
        return False

    @property
    def is_computer_win(self) -> False:
        return False

    @property
    def is_draw(self) -> False:
        return False

    def human_go(self, game: 'TicTacToe'):
        pass

    def computer_go(self, game: 'TicTacToe'):
        pass


class HumanTurn(IGameState):
    @property
    def is_human_win(self) -> False:
        return False

    @property
    def is_computer_win(self) -> False:
        return False

    @property
    def is_draw(self) -> False:
        return False

    def human_go(self, game: 'TicTacToe'):
        pass

    def computer_go(self, game: 'TicTacToe'):
        pass


class HumanWin(IGameState):
    @property
    def is_human_win(self) -> True:
        return True

    @property
    def is_computer_win(self) -> False:
        return False

    @property
    def is_draw(self) -> False:
        return False

    def human_go(self, game: 'TicTacToe'):
        pass

    def computer_go(self, game: 'TicTacToe'):
        pass


class ComputerWin(IGameState):
    @property
    def is_human_win(self) -> False:
        return False

    @property
    def is_computer_win(self) -> True:
        return True

    @property
    def is_draw(self) -> False:
        return False

    def human_go(self, game: 'TicTacToe'):
        pass

    def computer_go(self, game: 'TicTacToe'):
        pass


class Draw(IGameState):
    @property
    def is_human_win(self) -> False:
        return False

    @property
    def is_computer_win(self) -> False:
        return False

    @property
    def is_draw(self) -> True:
        return True

    def human_go(self, game: 'TicTacToe'):
        pass

    def computer_go(self, game: 'TicTacToe'):
        pass


class Cell:
    is_free = True
    value = 0

    def __bool__(self) -> bool:
        return self.is_free

    def __repr__(self):
        return f"cell: {self.value}"

    def reset(self):
        self.is_free = True
        self.value = 0


class TicTacToe:
    """ Tic-tac-toe game field.
    Allows access to fields by [i, j] index,
    also supports [:, j] and [i, :] indexes for GETTING item.
    """

    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    POLE_SIZE = 3
    _states: Dict[GameState, IGameState]
    _state = NotStarted()
    pole: Tuple[Tuple[Cell, ...], ...]

    def __init__(self):
        self._states = {
            GameState.NOT_STARTED: NotStarted(),
            GameState.COMPUTER_TURN: ComputerTurn(),
            GameState.HUMAN_TURN: HumanTurn(),
            GameState.COMPUTER_WIN: ComputerWin(),
            GameState.HUMAN_WIN: HumanWin(),
            GameState.DRAW: Draw(),
        }

    def __setitem__(self, key: Tuple[int, int], value: int):
        self._check_index(key)
        self._check_if_cell_is_free(key)
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False

    def __getitem__(self, item: tuple) -> Tuple[int, ...]:
        """ Return item or tuple of items, depending on input index. """
        self._check_index(item)
        x, y = item
        if isinstance(x, slice):
            return self._get_column(item[1])
        elif isinstance(y, slice):
            return self._get_row(item[0])

        return self.pole[x][y].value

    def __bool__(self):
        pass

    def __repr__(self):
        return '\n'.join(
            ' '.join(' | ' if cell.value == self.FREE_CELL
                     else 'O' if cell.value == self.COMPUTER_O else 'X'
                     for cell in row)
            for row in self.pole
        )

    @property
    def is_human_win(self):
        return self._state.is_human_win

    @property
    def is_computer_win(self):
        return self._state.is_computer_win

    @property
    def is_draw(self):
        return self._state.is_draw

    @property
    def state(self) -> IGameState:
        return self._state

    @state.setter
    def state(self, state: GameState):
        self._state = self._states[state]

    def init(self):
        if hasattr(self, 'pole'):
            self._clear()
        else:
            self.pole = tuple(
                tuple(Cell() for _ in range(self.POLE_SIZE))
                for _ in range(self.POLE_SIZE)
            )

    def human_go(self):
        self._state.human_go(self)
        # i, j = input('Введите координаты клетки в формате "i j"').split()

    def computer_go(self):
        self._state.computer_go(self)

    def show(self):
        for row in self.pole:
            print(' '.join(
                ' | ' if cell.value == self.FREE_CELL
                else 'O' if cell.value == self.COMPUTER_O else 'X'
                for cell in row
            ))

    def _clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].reset()

    def _get_row(self, row_index) -> Tuple[int, ...]:
        return tuple(cell.value for cell in self.pole[row_index])

    def _get_column(self, column_index: int) -> Tuple[int, ...]:
        return tuple(row[column_index].value for row in self.pole)

    @classmethod
    def _check_index(cls, index: Any):
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError('неверный индекс клетки')

        if all(type(e) is int for e in index):
            cls._check_single_elem_index(index)  # type: ignore
        else:
            raise IndexError('неверный индекс клетки')

    @classmethod
    # no need in this method!!
    def _check_single_elem_index(cls, single_index: Tuple[int, int]):
        if not all(0 <= e <= cls.POLE_SIZE - 1
                   for e in single_index):
            raise IndexError('неверный индекс клетки')

    def _check_if_cell_is_free(self, index: Tuple[int, int]):
        if not self.pole[index[0]][index[1]]:
            raise ValueError('клетка уже занята')


if __name__ == '__main__':
    game = TicTacToe()
    game.init()
    game.show()
