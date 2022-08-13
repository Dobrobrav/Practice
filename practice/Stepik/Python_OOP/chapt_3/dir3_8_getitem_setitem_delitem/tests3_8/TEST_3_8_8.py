import pytest
from random import randint
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
    assert bool(cell) == cell.is_free


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


@pytest.mark.parametrize('index, allow_slices', (
        (1, True),
        ((1, 3), True),
        ((slice(0, None, None), 5), True),
        ((0.5, 6), True),
        ('slfkjd', True),
        ((-5.5), True),
        (([1, 2, 3]), True),
        (int, True),
        ((1, 2, 3), True),
        ((1, 2, 3), False),
        (1, False),
        ((1, 3), False),
        ((slice(0, None, None), 5), False),
        ((0.5, 6), False),
        ('slfkjd', False),
        ((-5.5), False),
        (([1, 2, 3]), False),
        (int, False),
))
def test_check_index_allow_slices(index, allow_slices):
    with pytest.raises(IndexError):
        TicTacToe._check_index(index, allow_slices=allow_slices)


def test_check_if_slice_is_free_true():
    """ No error must be raised. """
    t = TicTacToe()
    t.pole[2][2].is_free = True
    t._check_if_cell_is_free((2, 2))


def test_check_if_slice_is_free_false():
    with pytest.raises(ValueError):
        t = TicTacToe()
        t.pole[2][2].is_free = False
        t._check_if_cell_is_free((2, 2))


def test_clear():
    t = TicTacToe()

    for i in range(3):
        for j in range(3):
            t.pole[i][j].value = randint(0, 2)

    t.clear()
    assert all(
        all(cell.is_free and cell.value == 0 for cell in row)
        for row in t.pole
    )


if __name__ == '__main__':
    pytest.main()
