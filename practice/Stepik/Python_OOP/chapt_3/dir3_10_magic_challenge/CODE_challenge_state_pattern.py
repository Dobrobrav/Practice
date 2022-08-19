from typing import Tuple, Any, Dict, Optional
from abc import ABC, abstractmethod
from enum import Enum

GamePole = Tuple[Tuple['Cell', ...], ...]


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
    def human_go(self, game_pole: GamePole) -> Optional[GameState]:
        ...

    @abstractmethod
    def computer_go(self, game_pole: GamePole) -> Optional[GameState]:
        ...

    @staticmethod
    def _print_computer_won():
        print("The game is finished and computer won!")

    @staticmethod
    def _print_human_won():
        print("The game is finished and human won!")

    @staticmethod
    def _print_draw():
        print("The game is finished and there's not winner!")

    @staticmethod
    def _request_coords() -> Tuple[int, int]:
        i, j = input("Type coordinates in the 'i, j' format").split(", ")
        coords = (int(i), int(j))
        return coords

    @staticmethod
    def _generate_coords() -> Tuple[int, int]:
        pass

    def _validate_coords(self, coords: Tuple[int, int]) -> bool:
        pass

    def _draw_sign(self, game_pole: GamePole,
                   coords: Tuple[int, int], sign: str):
        pass

    def _define_turn_result(self, game_pole: GamePole) -> GameState:
        pass


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

    def human_go(self, game_pole: GamePole) -> GameState.COMPUTER_TURN:
        coords = self._request_coords()
        while not self._validate_coords(coords):
            coords = self._request_coords()
        self._draw_sign(game_pole, coords, 'X')
        return GameState.COMPUTER_TURN

    def computer_go(self, game_pole: GamePole) -> GameState.HUMAN_TURN:
        coords = self._generate_coords()
        while not self._validate_coords(coords):
            coords = self._generate_coords()
        self._draw_sign(game_pole, coords, 'O')
        return GameState.HUMAN_TURN


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

    def human_go(self, game_pole: GamePole):
        print("It's computer's turn now!")

    def computer_go(self, game_pole: GamePole) -> GameState:
        self._draw_sign(game_pole, 'O')
        return self._define_turn_result(game_pole)


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

    def human_go(self, game_pole: GamePole) -> GameState:
        self._draw_sign(game_pole, 'X')
        return self._define_turn_result(game_pole)

    def computer_go(self, game_pole: GamePole):
        print("It's human's turn now!")


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

    def human_go(self, game_pole: GamePole):
        self._print_human_won()

    def computer_go(self, game_pole: GamePole):
        self._print_human_won()


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

    def human_go(self, game_pole: GamePole):
        self._print_computer_won()

    def computer_go(self, game_pole: GamePole):
        self._print_computer_won()


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

    def human_go(self, game_pole: GamePole):
        self._print_draw()

    def computer_go(self, game_pole: GamePole):
        self._print_draw()


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
        # need to wrap it with smt more beautiful and readable
        # like the consept that the state methods return the new state
        new_state = self._states.get(self._state.human_go(self.pole))
        if new_state:
            self._state = new_state
        # i, j = input('Введите координаты клетки в формате "i j"').split()

    def computer_go(self):
        new_state = self._states.get(self._state.computer_go(self.pole))
        if new_state:
            self._state = new_state

    def show(self):
        for row in self.pole:
            print(' '.join(
                ' | ' if cell.value == self.FREE_CELL
                else 'O' if cell.value == self.COMPUTER_O else 'X'
                for cell in row
            ))

    def _get_winner(self) -> GameState:
        pass

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
