import pytest
from UTILS_3_9_8 import *


@pytest.fixture
def stack():
    stack = Stack()
    return stack


@pytest.fixture
def stack_obj():
    stack_obj = StackObj('some data')
    return stack_obj


def get_node(stack: Stack, key: int) -> StackObj:
    node = stack.top
    for _ in range(key):
        node = node.next
    return node


def test_stack_obj_init(stack_obj):
    assert stack_obj.data == 'some data' and stack_obj.next is None


def test_stack_init(stack):
    assert stack.top is None and stack._length == 0


def test_stack_obj_next(stack_obj):
    other_stack_obj = StackObj('other data')
    stack_obj.next = other_stack_obj
    assert stack_obj.next is other_stack_obj


@pytest.mark.parametrize('index', (0, 1, 2, 4, 10))
def test_stack_add(stack, stack_obj, index):
    for i in range(index):
        push_back(stack, StackObj(str(i)))
    res = stack + stack_obj
    assert res is stack and get_node(stack, index) is stack_obj


@pytest.mark.parametrize('index', (0, 1, 2, 4, 10))
def test_stack_iadd(stack, stack_obj, index):
    for i in range(index):
        push_back(stack, StackObj(str(i)))
    stack_save = stack
    stack += stack_obj
    assert stack_save is stack and get_node(stack, index) is stack_obj


@pytest.mark.parametrize('flag', (True, False))
def test_stack_mul(stack, stack_obj, flag):
    if flag:
        push_back(stack, stack_obj)
    stack_objects_to_add = [str(i) for i in range(10)]
    are_objects_same = all(
        a == b.data
        for a, b in zip(stack_objects_to_add, get_nodes(stack)[flag:])
    )

    assert stack * stack_objects_to_add is stack and are_objects_same


@pytest.mark.parametrize('flag', (True, False))
def test_stack_imul(stack, stack_obj, flag):
    if flag:
        push_back(stack, stack_obj)
    stack_objects_to_add = [str(i) for i in range(10)]
    stack_save = stack
    stack *= stack_objects_to_add
    are_objects_same = all(
        a == b.data
        for a, b in zip(stack_objects_to_add, get_nodes(stack)[flag:])
    )
    assert stack_save is stack and are_objects_same


@pytest.mark.parametrize('index, stack_size', (
        (0, 1),
        (0, 10),
        (1, 2),
        (1, 10),
        (2, 10),
        (4, 10),
        (6, 10),
))
def test_stack_setitem_in_long_stack(stack, stack_obj, index, stack_size):
    for i in range(stack_size):
        push_back(stack, StackObj(str(i)))
    stack[index] = stack_obj.data
    assert get_node(stack, index).data == stack_obj.data


def test_stack_setitem_error(stack):
    pass


def test_stack_getitem(stack):
    pass


def test_stack_getitem_error(stack):
    pass


def test_stack_iter(stack):
    pass


def test_stack_len(stack):
    pass


def test_stack_push_back(stack):
    pass


def test_stack_push_front(stack):
    pass


def test_stack_pop(stack):
    pass


def test_stack_(stack):
    pass


def test_stack_():
    pass


def test_stack_():
    pass


if __name__ == '__main__':
    pytest.main()
