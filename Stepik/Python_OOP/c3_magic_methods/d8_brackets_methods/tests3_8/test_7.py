import pytest
from practice.Stepik.Python_OOP.c3_magic_methods.dir3_8_getitem_setitem_delitem \
    .CODE_3_8_7 import *


@pytest.mark.parametrize('test_coords', [
    [],
    [1, -2, 3],
    [1.5],
    [-0.6, 2],
])
def test_init(test_coords):
    vector = RadiusVector(*test_coords)
    assert vector.coords == test_coords


@pytest.mark.parametrize('key, value', [
    (0, 1),
    (4, 5),
    (2, 3),
    (slice(4), (1, 2, 3, 4)),
    (slice(1, 4), (2, 3, 4)),
    (slice(None, None, -1), (5, 4, 3, 2, 1))
])
def test_getitem(key, value):
    start_coords = [1, 2, 3, 4, 5]
    vector = RadiusVector()
    vector.coords = start_coords
    assert vector[key] == value


@pytest.mark.parametrize('key, value', [
    (0, 5),
    (4, -4),
    (2, 0),
    (slice(4), (1, 2, 3, 4)),
    (slice(1, 4), (2, 3, 4)),
    (slice(None, None, -1), (5, 4, 3, 2, 1))
])
def test_setitem(key, value):
    start_coords = [1, 2, 3, 4, 5]
    vector = RadiusVector()
    vector.coords = start_coords

    vector[key] = value
    start_coords[key] = value

    assert vector.coords == start_coords


if __name__ == '__main__':
    pytest.main()
