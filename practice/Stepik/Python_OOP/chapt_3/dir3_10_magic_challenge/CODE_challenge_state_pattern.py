from typing import Tuple, Any, Dict, Callable, Literal
from abc import ABC, abstractmethod
from enum import Enum
from random import randint

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
        print("The game is finished and computer won!")

    @staticmethod
    def _print_human_won():
        print("The game is finished and human won!")

    @staticmethod
    def _print_draw():
        print("The game is finished and there's no winner!")

    def _get_valid_coords(self, game_pole: GamePole,
                          get_coords: Callable) -> Tuple[int, int]:
        coords = get_coords()
        while not self._validate_coords(game_pole, coords):
            coords = get_coords()
        return coords

    @staticmethod
    def _request_coords() -> Tuple[int, int]:
        i, j = input("Type coordinates in the 'i j' format ").split(", ")
        coords = (int(i), int(j))
        return coords

    @staticmethod
    def _generate_coords() -> Tuple[int, int]:
        coords = (randint(0, 2), randint(0, 2))
        return coords

    def _validate_coords(self, game_pole: GamePole,
                         coords: Any) -> bool:
        if self._validate_coords_type(coords):
            i, j = coords
            if game_pole[i][j]:
                return True

        return False

    @staticmethod
    def _validate_coords_type(coords: Any) -> bool:
        return (isinstance(coords, tuple) and len(coords) == 2
                and all(type(coord) is int for coord in coords))

    @staticmethod
    def _draw_sign(game_pole: GamePole,
                   coords: Tuple[int, int], sign: int):
        i, j = coords
        game_pole[i][j].value = sign

    def define_turn_result(self, game_pole: GamePole,
                           current_state: GameState) -> GameState:
        is_computer_win = self._has_victory_line(
            game_pole,
            TicTacToe.COMPUTER_O,
        )
        if is_computer_win:
            return GameState.COMPUTER_WIN
        is_human_win = self._has_victory_line(
            game_pole,
            TicTacToe.HUMAN_X,
        )
        if is_human_win:
            return GameState.HUMAN_WIN
        has_free_cells = any(game_pole[i][j].value == TicTacToe.FREE_CELL
                             for i in range(TicTacToe.POLE_SIZE)
                             for j in range(TicTacToe.POLE_SIZE))
        if has_free_cells and current_state is GameState.COMPUTER_TURN:
            return GameState.HUMAN_TURN
        if has_free_cells and current_state is GameState.HUMAN_TURN:
            return GameState.COMPUTER_TURN
        if not has_free_cells:
            return GameState.DRAW
        raise RuntimeError

    @staticmethod
    def _has_victory_line(game_pole: GamePole, sign: int) -> bool:
        hor_lines = any(all(cell.value == sign for cell in row)
                        for row in game_pole)
        vert_lines = any(all(cell.value == sign for cell in row)
                         for row in zip(*game_pole))
        main_diagonal = all(game_pole[coord][coord].value == sign
                            for coord in range(TicTacToe.POLE_SIZE - 1, -1, -1))
        sub_diagonal = all(game_pole[i][j].value == sign
                           for i, j in zip(range(TicTacToe.POLE_SIZE),
                                           range(TicTacToe.POLE_SIZE - 1, -1, -1)))
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
        self._draw_sign(game_pole, coords, TicTacToe.HUMAN_X)
        return GameState.COMPUTER_TURN

    def computer_go(self, game_pole: GamePole) -> Literal[GameState.HUMAN_TURN]:
        coords = self._get_valid_coords(game_pole, self._generate_coords)
        self._draw_sign(game_pole, coords, TicTacToe.COMPUTER_O)
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
        self._draw_sign(game_pole, coords, TicTacToe.COMPUTER_O)
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
        self._draw_sign(game_pole, coords, TicTacToe.HUMAN_X)
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
    _states: Dict[GameState, IGameState]
    _state: IGameState = NotStarted()
    pole: Tuple[Tuple[Cell, ...], ...]

    def __init__(self):
        self.init()
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
        new_state = self._state.define_turn_result(self.pole,
                                                   GameState.HUMAN_TURN)
        if new_state is not None:
            self.state = new_state  # type: ignore
        self.show()

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
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")
