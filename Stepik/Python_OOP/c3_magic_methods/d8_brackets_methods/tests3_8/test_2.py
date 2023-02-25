import pytest
from practice.Stepik.Python_OOP.c3_magic_methods.dir3_8_getitem_setitem_delitem\
    .CODE_3_8_2 import *


@pytest.mark.parametrize('data, attrs',
                         [({'id': 1, 'name': 'some_name', 'age': 18},
                           ('id', 'name', 'age')),
                          ({'id2': 2, 'name2': 'some_name2', 'age2': -182},
                           ('id2', 'name2', 'age2')),
                          ({'id3': 3, 'name3': 'some_name3', 'age3': 0.6},
                           ('id3', 'name3', 'age3')),
                          ({'id4': 4, 'name4': 'some_name4', 'age4': -18.5},
                           ('id4', 'name4', 'age4'))])
def test_record_init(data, attrs):
    record = Record(**data)
    assert record.__dict__ == data | {'_key_by_id': attrs}


if __name__ == '__main__':
    pytest.main()
