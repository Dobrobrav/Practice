import pytest
from practice.Stepik.Python_OOP.c3_magic_methods.dir3_8_getitem_setitem_delitem \
    .CODE_3_8_9 import *


@pytest.fixture
def bag():
    bag = Bag(1000)
    return bag


def test_thing_init():
    thing = Thing('some thing', 10)
    assert (thing.name, thing.weight) == ('some thing', 10)


def test_bag_init(bag):
    assert ((bag._max_weight, bag._current_weight, bag._things)
            == (1000, 0, []))


@pytest.mark.parametrize('thing, index', (
        (Thing('some thing', 10), 0),
        (Thing('some thing', 10), 1),
        (Thing('some thing', 10), 4),
))
def test_bag_add_thing(bag, thing, index):
    for _ in range(index):
        bag._things.append(Thing('plug', 0))
    bag.add_thing(thing)

    assert bag._things[index] is thing


def test_bag_add_thing_error(bag):
    bag._current_weight = 1000
    with pytest.raises(ValueError):
        bag.add_thing(Thing('other thing', 1))


@pytest.mark.parametrize('thing, index', (
        (Thing('some thing', 10), 0),
        (Thing('some thing', 10), 1),
        (Thing('some thing', 10), 4),
))
def test_bag_setitem(bag, thing, index):
    for i in range(index + 2):
        bag._things.append(Thing('plug', i))
    bag[index] = thing

    assert bag._things[index] is thing


@pytest.mark.parametrize('thing, index, error', (
        (Thing('some thing', 501), 0, ValueError),
        (Thing('some thing', 1), 2, IndexError),
        (Thing('some thing', 1), 0.5, IndexError),
        (Thing('some thing', 1), -3, IndexError),
))
def test_bag_setitem_error(bag, thing, index, error):
    for _ in range(2):
        bag._things.append(Thing('plug', 500))
    bag._current_weight = 1000
    with pytest.raises(error):
        bag[index] = thing


@pytest.mark.parametrize('thing, index', (
        (Thing('some thing', 10), 0),
        (Thing('some thing', 10), 1),
        (Thing('some thing', 10), 4),
))
def test_bag_getitem(bag, thing, index):
    for _ in range(index):
        bag.add_thing(Thing('plug', 0))
    bag.add_thing(thing)

    assert bag[index] is thing


@pytest.mark.parametrize('thing, test_index,', (
        (Thing('some thing', 1), 0),
        (Thing('some thing', 1), 1),
        (Thing('some thing', 1), 10),
        (Thing('some thing', 1), 0.5),
        (Thing('some thing', 1), 0.6),
        (Thing('some thing', 1), 0.0),
        (Thing('some thing', 1), -1),
        (Thing('some thing', 1), -3),
))
def test_bag_getitem_error(bag, thing, test_index):
    with pytest.raises(IndexError):
        _ = bag[test_index]


@pytest.mark.parametrize('index, weight_left_after_del', (
        (0, 500),
        (1, 400),
        (2, 300),
))
def test_bag_delitem(bag, index, weight_left_after_del):
    for i in range(3):
        bag._things.append(Thing(str(i), (i + 1) * 100))
    bag._current_weight = 600
    things_reference = bag._things.copy()

    del bag[index]
    del things_reference[index]
    assert (bag._things == things_reference
            and bag._current_weight == weight_left_after_del)


@pytest.mark.parametrize('index', (0.5, 5.5, 0, 1, 2, 10))
def test_bag_delitem_error(bag, index):
    with pytest.raises(IndexError):
        del bag[index]


if __name__ == '__main__':
    pytest.main()
