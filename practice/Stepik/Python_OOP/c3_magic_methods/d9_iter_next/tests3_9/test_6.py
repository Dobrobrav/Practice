import pytest
from practice.Stepik.Python_OOP.c3_magic_methods.d9_iter_next \
    .code_6 import *


@pytest.fixture
def init_list():
    lst = [['x00', 'x01', 'x02'],
           ['x10', 'x11'],
           ['x20', 'x21', 'x22', 'x23', 'x24'],
           ['x30', 'x31', 'x32', 'x33']]
    return lst


@pytest.fixture
def iterator(init_list):
    iterator = TriangleListIterator(init_list)
    return iterator


def test_triangle_list_iterator_init(init_list, iterator):
    assert init_list is iterator.lst


def test_triangle_list_iterator_iter(iterator):
    assert list(iter(iterator)) == ['x00',
                                    'x10', 'x11',
                                    'x20', 'x21', 'x22',
                                    'x30', 'x31', 'x32', 'x33']


def test_triangle_list_iterator_iter_error():
    iterator = TriangleListIterator([['x00', 'x01', 'x02'],
                                     ['x20', 'x21', 'x22'],
                                     ['x10', 'x11'],
                                     ['x30', 'x31', 'x32', 'x33']])
    with pytest.raises(IndexError):
        list(iter(iterator))


if __name__ == '__main__':
    pytest.main()
