import pytest
from practice.Stepik.Python_OOP.chapt_3.dir3_8_getitem_setitem_delitem \
    .CODE_3_8_3 import *


def test_index_error_getitem():
    with pytest.raises(IndexError):
        tr = Track(0, 0)
        _ = tr[0]


def test_index_error_setitem():
    with pytest.raises(IndexError):
        tr = Track(0, 0)
        tr[0] = 5


if __name__ == '__main__':
    pytest.main()
