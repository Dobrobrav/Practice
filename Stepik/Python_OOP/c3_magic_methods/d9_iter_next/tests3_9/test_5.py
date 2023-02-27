import pytest
from Stepik.Python_OOP.c3_magic_methods.d9_iter_next \
    .code_5 import *


@pytest.fixture
def person():
    person = Person('Bill Gates', 'businessman', 61, 1_000_000, 46)
    return person


def test_person_init(person):
    is_dict_correct = person.__dict__ == {
        'fio': 'Bill Gates', 'job': 'businessman',
        'old': 61, 'salary': 1000000, 'year_job': 46
    }
    is_name_by_index_correct = (person._attr_name_by_index
                                == ('fio', 'job', 'old', 'salary', 'year_job'))
    assert (is_dict_correct
            and is_name_by_index_correct
            and person._current_iter_index == 0)


@pytest.mark.parametrize('attr_name, index, value', (
        ('fio', 0, 'balak'),
        ('job', 1, 'teacher'),
        ('old', 2, 37),
        ('salary', 3, 100_000),
        ('year_job', 4, 12),
))
def test_person_setitem_single_value(person, attr_name, index, value):
    person[index] = value
    assert getattr(person, attr_name) == value


def test_person_setitem_many_together(person):
    for i, value in zip(range(5), ('balak', 'teacher', 37, 100_000, 12)):
        person[i] = value
    assert all(
        getattr(person, attr_name) == value
        for attr_name, value in zip(
            ('fio', 'job', 'old', 'salary', 'year_job'),
            ('balak', 'teacher', 37, 100_000, 12)
        )
    )


@pytest.mark.parametrize('index', (5, 8, -1, -3, 3.5, -2.5))
def test_person_setitem_error(index, person):
    with pytest.raises(IndexError):
        person[index] = 'plug'


@pytest.mark.parametrize('index, value', (
        (0, 'Bill Gates'),
        (1, 'businessman'),
        (2, 61),
        (3, 1_000_000),
        (4, 46),
))
def test_person_getitem(person, index, value):
    assert person[index] == value


@pytest.mark.parametrize('index', (5, 8, -1, -3, 3.5, -2.5))
def test_person_getitem_error(person, index):
    with pytest.raises(IndexError):
        _ = person[index]


def test_person_iter(person):
    person._current_iter_index = 5
    it = iter(person)
    assert it is person and person._current_iter_index == 0


def test_person_next(person):
    assert (('Bill Gates', 'businessman', 61, 1_000_000, 46)
            == tuple(value for value in person))


def test_person_next_error(person):
    it = iter(person)
    for _ in range(5):
        next(it)
    with pytest.raises(StopIteration):
        next(it)


if __name__ == '__main__':
    pytest.main()
