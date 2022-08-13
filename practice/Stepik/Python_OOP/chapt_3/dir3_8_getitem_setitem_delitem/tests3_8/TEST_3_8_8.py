import pytest
from typing import Iterable
from practice.Stepik.Python_OOP.chapt_3.dir3_8_getitem_setitem_delitem \
    .CODE_3_8_8 import *


def test_init():
    t = TicTacToe()
    assert all(
        all(cell.value == 0 for cell in row)
        for row in t.pole
    )


@pytest.mark.parametrize('value', (True, False))
def test_cell_bool(value: bool):
    cell = Cell()
    cell.is_free = value
    assert bool(cell) == value


@pytest.mark.parametrize('values', (
        (1, 2, 2, 2, 1, 1, 1, 2, 1),
        (2, 1, 2, 1, 2, 1, 1, 1, 2),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2, 2, 2, 2),
))
def test_setitem(values: Iterable):
    print(values)
    t = TicTacToe()
    it = iter(values)

    for i in range(3):
        for j in range(3):
            t[i, j] = next(it)

    it = iter(values)
    assert all(
        all(cell.value == next(it) for cell in row)
        for row in t.pole
    )


@pytest.mark.parametrize('values', (
        (1, 2, 2, 2, 1, 1, 1, 2, 1),
        (2, 1, 2, 1, 2, 1, 1, 1, 2),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (1, 1, 1, 1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2, 2, 2, 2),
))
def test_getitem_single(values: Iterable):
    t = TicTacToe()
    it = iter(values)

    for i in range(3):
        for j in range(3):
            t.pole[i][j].value = next(it)

    it = iter(values)

    assert all(
        all(t[i, j] == next(it) for j in range(3))
        for i in range(3)
    )


@pytest.mark.parametrize('values', (
        ((1, 2, 2), (2, 1, 1), (1, 2, 1)),
        ((2, 1, 2), (1, 2, 1), (1, 1, 2)),
        ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
        ((1, 1, 1), (1, 1, 1), (1, 1, 1)),
        ((2, 2, 2), (2, 2, 2), (2, 2, 2)),
))
def test_getitem_slice(values: tuple):
    t = TicTacToe()
    it = iter(values)

    for i in range(3):
        row = next(it)
        for j in range(3):
            t.pole[i][j].value = row[j]

    assert (all(t[i, :] == values[i] for i in range(3))
            and all(t[:, j] == tuple(row[j].value for row in t.pole)
                    for j in range(3)))


def test_get_row():
    pass  # maybe I should move the code from the function above here


def test_get_column():
    pass  # and here. And then delete the upper test (maybe not)


def test_check_index():
    pass


def test_single_elem_index():
    pass


def test_check_slice_index():
    pass


def test_check_if_slice_is_free():
    pass


def test_clear():
    pass


if __name__ == '__main__':
    pytest.main()
