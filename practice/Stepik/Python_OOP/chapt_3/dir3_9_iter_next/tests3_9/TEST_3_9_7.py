import pytest
from practice.Stepik.Python_OOP.chapt_3.dir3_9_iter_next \
    .CODE_3_9_7 import *


@pytest.fixture
def lst():
    lst = [['x00', 'x01', 'x02'],
           ['x10', 'x11', 'x12'],
           ['x20', 'x21', 'x22'],
           ['x30', 'x31', 'x32']]
    return lst


@pytest.fixture
def iterator(lst):
    iterator = IterColumn(lst, 1)
    return iterator


def test_iter_column_init(lst, iterator):
    assert iterator.lst == lst and iterator.column == 1


def test_iter_column_iter(lst, iterator):
    assert (list(value for value in iter(iterator))
            == list(row[1] for row in lst))


if __name__ == '__main__':
    pytest.main()
