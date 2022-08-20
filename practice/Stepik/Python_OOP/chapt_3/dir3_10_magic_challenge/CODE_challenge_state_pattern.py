from typing import Any, Callable, Literal, TypeAlias
from abc import ABC, abstractmethod
from enum import Enum
from random import randint

GamePole: TypeAlias = tuple[tuple['Cell', ...], ...]


class GameState(Enum):
    NOT_STARTED = 0
    COMPUTER_TURN = 1
    HUMAN_TURN = 2
    COMPUTER_WIN = 3
    HUMAN_WIN = 4
    DRAW = 5


class IGameState(ABC):
    def __init__(self, game: 'TicTacToe'):
        self.game = game

    @property
    @abstractmethod
    def state_enum(self) -> GameState:
        ...

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
    def human_go(self, game_pole: GamePole) -> GameState:
        ...

    @abstractmethod
    def computer_go(self, game_pole: GamePole) -> GameState:
        ...

    @staticmethod
    def _print_computer_won():
        pass
        # print("The game is finished and computer won!")

    @staticmethod
    def _print_human_won():
        pass
        # print("The game is finished and human won!")

    @staticmethod
    def _print_draw():
        pass
        # print("The game is finished and there's no winner!")

    def _get_valid_coords(self, game_pole: GamePole,
                          get_coords: Callable) -> tuple[int, int]:
        coords = get_coords()
        while not self._validate_coords(game_pole, coords):
            coords = get_coords()
        return coords

    def _request_coords(self) -> tuple[int, int]:
        separator = " "
        try:
            i, j = input(f"Type coordinates in the 'i{separator}j' format ") \
                .split(" ")
            return int(i), int(j)
        except ValueError:
            return self._request_coords()

    @staticmethod
    def _generate_coords() -> tuple[int, int]:
        coords = (randint(0, 2), randint(0, 2))
        return coords

    def _validate_coords(self, game_pole: GamePole, coords: Any) -> bool:
        if (self._validate_coords_structure(coords)
                and self._validate_coords_range(coords)):
            i, j = coords
            if game_pole[i][j]:
                return True

        return False

    def _validate_coords_range(self, coords: tuple[int, int]) -> bool:
        return all(0 <= coord <= self.game.POLE_SIZE for coord in coords)

    @staticmethod
    def _validate_coords_structure(coords: Any) -> bool:
        return (isinstance(coords, tuple) and len(coords) == 2
                and all(type(coord) is int for coord in coords))

    @staticmethod
    def _draw_sign(game_pole: GamePole,
                   coords: tuple[int, int], sign: int):
        i, j = coords
        game_pole[i][j].value = sign

    def define_turn_result(self, game_pole: GamePole,
                           current_state: GameState) -> GameState:
        is_computer_win = self._has_victory_line(
            game_pole,
            self.game.COMPUTER_O,
        )
        if is_computer_win:
            return GameState.COMPUTER_WIN
        is_human_win = self._has_victory_line(
            game_pole,
            self.game.HUMAN_X,
        )
        if is_human_win:
            return GameState.HUMAN_WIN
        has_free_cells = any(game_pole[i][j].value == self.game.FREE_CELL
                             for i in range(self.game.POLE_SIZE)
                             for j in range(self.game.POLE_SIZE))
        if has_free_cells and current_state is GameState.COMPUTER_TURN:
            return GameState.HUMAN_TURN
        if has_free_cells and current_state is GameState.HUMAN_TURN:
            return GameState.COMPUTER_TURN
        if not has_free_cells:
            return GameState.DRAW
        raise RuntimeError

    def _has_victory_line(self, game_pole: GamePole, sign: int) -> bool:
        hor_lines = any(all(cell.value == sign for cell in row)
                        for row in game_pole)
        vert_lines = any(all(cell.value == sign for cell in row)
                         for row in zip(*game_pole))
        main_diagonal = all(
            game_pole[coord][coord].value == sign
            for coord in range(self.game.POLE_SIZE - 1, -1, -1)
        )
        sub_diagonal = all(
            game_pole[i][j].value == sign
            for i, j in zip(range(self.game.POLE_SIZE),
                            range(self.game.POLE_SIZE - 1, -1, -1))
        )
        return hor_lines or vert_lines or main_diagonal or sub_diagonal


class NotStarted(IGameState):
    @property
    def state_enum(self) -> Literal[GameState.NOT_STARTED]:
        return GameState.NOT_STARTED

    @property
    def is_human_win(self) -> Literal[False]:
        return False

    @property
    def is_computer_win(self) -> Literal[False]:
        return False

    @property
    def is_draw(self) -> Literal[False]:
        return False

    def human_go(self, game_pole: GamePole) -> Literal[GameState.COMPUTER_TURN]:
        coords = self._get_valid_coords(game_pole, self._request_coords)
        self._draw_sign(game_pole, coords, self.game.HUMAN_X)
        return GameState.COMPUTER_TURN

    def computer_go(self, game_pole: GamePole) -> Literal[GameState.HUMAN_TURN]:
        coords = self._get_valid_coords(game_pole, self._generate_coords)
        self._draw_sign(game_pole, coords, self.game.COMPUTER_O)
        return GameState.HUMAN_TURN


class ComputerTurn(IGameState):
    @property
    def state_enum(self) -> Literal[GameState.COMPUTER_TURN]:
        return GameState.COMPUTER_TURN

    @property
    def is_human_win(self) -> Literal[False]:
        return False

    @property
    def is_computer_win(self) -> Literal[False]:
        return False

    @property
    def is_draw(self) -> Literal[False]:
        return False

    def human_go(self, game_pole: GamePole):
        print("It's computer's turn now!")

    def computer_go(self, game_pole: GamePole) -> GameState:
        coords = self._get_valid_coords(game_pole, self._generate_coords)
        self._draw_sign(game_pole, coords, self.game.COMPUTER_O)
        return self.define_turn_result(game_pole, GameState.COMPUTER_TURN)


class HumanTurn(IGameState):
    @property
    def state_enum(self) -> Literal[GameState.HUMAN_TURN]:
        return GameState.HUMAN_TURN

    @property
    def is_human_win(self) -> Literal[False]:
        return False

    @property
    def is_computer_win(self) -> Literal[False]:
        return False

    @property
    def is_draw(self) -> Literal[False]:
        return False

    def human_go(self, game_pole: GamePole) -> GameState:
        coords = self._get_valid_coords(game_pole, self._request_coords)
        self._draw_sign(game_pole, coords, self.game.HUMAN_X)
        return self.define_turn_result(game_pole, GameState.HUMAN_TURN)

    def computer_go(self, game_pole: GamePole):
        print("It's human's turn now!")


class HumanWin(IGameState):
    def __bool__(self) -> Literal[False]:
        return False

    @property
    def state_enum(self) -> Literal[GameState.HUMAN_WIN]:
        return GameState.HUMAN_WIN

    @property
    def is_human_win(self) -> Literal[True]:
        return True

    @property
    def is_computer_win(self) -> Literal[False]:
        return False

    @property
    def is_draw(self) -> Literal[False]:
        return False

    def human_go(self, game_pole: GamePole):
        self._print_human_won()

    def computer_go(self, game_pole: GamePole):
        self._print_human_won()


class ComputerWin(IGameState):
    def __bool__(self) -> Literal[False]:
        return False

    @property
    def state_enum(self) -> Literal[GameState.COMPUTER_WIN]:
        return GameState.COMPUTER_WIN

    @property
    def is_human_win(self) -> Literal[False]:
        return False

    @property
    def is_computer_win(self) -> Literal[True]:
        return True

    @property
    def is_draw(self) -> Literal[False]:
        return False

    def human_go(self, game_pole: GamePole):
        self._print_computer_won()

    def computer_go(self, game_pole: GamePole):
        self._print_computer_won()


class Draw(IGameState):
    def __bool__(self) -> Literal[False]:
        return False

    @property
    def state_enum(self) -> Literal[GameState.DRAW]:
        return GameState.DRAW

    @property
    def is_human_win(self) -> Literal[False]:
        return False

    @property
    def is_computer_win(self) -> Literal[False]:
        return False

    @property
    def is_draw(self) -> Literal[True]:
        return True

    def human_go(self, game_pole: GamePole):
        self._print_draw()

    def computer_go(self, game_pole: GamePole):
        self._print_draw()


class Cell:
    value = 0

    def __bool__(self) -> bool:
        """ Return True if cell is free (value == 0)"""
        return not bool(self.value)

    def __repr__(self):
        return f"cell: {self.value}"

    def reset(self):
        self.value = 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    POLE_SIZE = 3
    _states: dict[GameState, IGameState]
    _state: IGameState
    pole: tuple[tuple[Cell, ...], ...]

    def __init__(self):
        self.init()
        self._states = {
            GameState.NOT_STARTED: NotStarted(self),
            GameState.COMPUTER_TURN: ComputerTurn(self),
            GameState.HUMAN_TURN: HumanTurn(self),
            GameState.COMPUTER_WIN: ComputerWin(self),
            GameState.HUMAN_WIN: HumanWin(self),
            GameState.DRAW: Draw(self),
        }
        self.state = GameState.NOT_STARTED

    def __setitem__(self, key: tuple[int, int], value: int):
        self._check_index(key)
        self._check_if_cell_is_free(key)
        self.pole[key[0]][key[1]].value = value
        new_state = self._state.define_turn_result(self.pole,
                                                   GameState.HUMAN_TURN)
        if new_state is not None:
            self.state = new_state  # type: ignore
        self.show()

    def __getitem__(self, item: tuple) -> tuple[int, ...]:
        """ Return item or tuple of items, depending on input index. """
        self._check_index(item)
        i, j = item
        return self.pole[i][j].value

    def __bool__(self):
        return bool(self.state)

    def __repr__(self):
        return '\n'.join(
            ' | '.join(' ' if cell.value == self.FREE_CELL
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
            self.state = GameState.NOT_STARTED
        else:
            self.pole = tuple(
                tuple(Cell() for _ in range(self.POLE_SIZE))
                for _ in range(self.POLE_SIZE)
            )

    def human_go(self):
        # need to wrap it with smt more beautiful and readable
        new_state = self._state.human_go(self.pole)
        if new_state is not None:
            self.state = new_state
        self.show()

    def computer_go(self):
        new_state = self._state.computer_go(self.pole)
        if new_state is not None:
            self.state = new_state

        self.show()

    def show(self):
        for row in self.pole:
            print(' | '.join(
                ' ' if cell.value == self.FREE_CELL
                else 'O' if cell.value == self.COMPUTER_O else 'X'
                for cell in row
            ))

    def _get_winner(self) -> GameState:
        pass

    def _clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].reset()

    def _get_row(self, row_index) -> tuple[int, ...]:
        return tuple(cell.value for cell in self.pole[row_index])

    def _get_column(self, column_index: int) -> tuple[int, ...]:
        return tuple(row[column_index].value for row in self.pole)

    @classmethod
    def _check_index(cls, index: Any):
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError('неверный индекс клетки')

        if all(type(e) is int for e in index):
            if not all(0 <= e <= cls.POLE_SIZE - 1
                       for e in index):
                raise IndexError('неверный индекс клетки')  # type: ignore
        else:
            raise IndexError('неверный индекс клетки')

    def _check_if_cell_is_free(self, index: tuple[int, int]):
        if not self.pole[index[0]][index[1]]:
            raise ValueError('клетка уже занята')


if __name__ == '__main__':
    game = TicTacToe()
    game.init()
