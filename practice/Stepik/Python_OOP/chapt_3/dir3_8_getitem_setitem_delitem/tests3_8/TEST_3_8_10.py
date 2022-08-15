import pytest
from practice.Stepik.Python_OOP.chapt_3.dir3_8_getitem_setitem_delitem \
    .CODE_3_8_10 import *


@pytest.fixture
def table():
    table = SparseTable()
    return table


@pytest.mark.parametrize('obj', (1, 'a', (1, 2, 3), [1, 2], 2.5, True))
def test_cell_init(obj):
    cell = Cell(obj)
    assert cell.value == obj


def test_table_init(table):
    assert ((table._table_map, table._cell_quantity_in_cols,
             table._cell_quantity_in_rows) == ({}, {}, {}))


def test_table_rows_property():



def test_table_cols_property():
    pass


def test_add_data():
    pass


def test_setitem():
    pass


def test_getitem_error():
    pass


def test_remove_data():
    pass


def test_remove_data_error():
    pass


if __name__ == '__main__':
    pytest.main()
