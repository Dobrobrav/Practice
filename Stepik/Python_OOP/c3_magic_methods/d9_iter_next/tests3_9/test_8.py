# TODO: refactor code (many duplicate lines)
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


@pytest.fixture
def compare_lst():
    compare_lst = [StackObj(str(i)) for i in range(20)]
    return compare_lst


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
def test_stack_setitem_in_stack(stack, stack_obj, index, stack_size):
    for i in range(stack_size):
        push_back(stack, StackObj(str(i)))
    stack[index] = stack_obj.data
    assert get_node(stack, index).data == stack_obj.data


@pytest.mark.parametrize('stack_length, index', (
        (0, 1),
        (1, 2),
        (10, 11),
        (0, 2),
        (1, 3),
        (10, 12),
        (10, 0.5),
        (10, 1.2),
        (10, -5),
        (10, -3.4),
))
def test_stack_setitem_error(stack, stack_obj, stack_length, index):
    for i in range(stack_length):
        push_back(stack, StackObj(str(i)))
    with pytest.raises(IndexError):
        stack[index] = 'some data'


@pytest.mark.parametrize('index, stack_size', (
        (0, 1),
        (0, 10),
        (1, 2),
        (1, 10),
        (2, 10),
        (4, 10),
        (6, 10),
))
def test_stack_getitem(stack, stack_obj, index, stack_size):
    for i in range(stack_size):
        push_back(stack, StackObj(str(i)))
    assert get_node(stack, index).data == stack[index]


@pytest.mark.parametrize('stack_length, index', (
        (0, 1),
        (1, 2),
        (10, 11),
        (0, 2),
        (1, 3),
        (10, 12),
        (10, 0.5),
        (10, 1.2),
        (10, -5),
        (10, -3.4),
))
def test_stack_getitem_error(stack, stack_obj, stack_length, index):
    for i in range(stack_length):
        push_back(stack, StackObj(str(i)))
    with pytest.raises(IndexError):
        _ = stack[index]


def test_stack_iter(stack, compare_lst):
    for stack_obj in compare_lst:
        push_back(stack, stack_obj)

    assert compare_lst == list(iter(stack))


@pytest.mark.parametrize('length', (x for x in range(50)))
def test_stack_len(stack, length):
    stack._length = length
    assert len(stack) == stack._length


def test_stack_push_back(stack, compare_lst):
    for stack_obj in compare_lst:
        stack.push_back(stack_obj)
    assert get_nodes(stack) == compare_lst


def test_stack_push_front(stack, compare_lst):
    for stack_obj in compare_lst:
        stack.push_front(stack_obj)
    assert get_nodes(stack) == compare_lst[::-1]


def test_stack_pop(stack, compare_lst):
    for stack_obj in compare_lst:
        stack.push_back(stack_obj)
    nodes_from_stack = [stack.pop() for _ in range(len(compare_lst))]
    assert nodes_from_stack == compare_lst[::-1] and get_nodes(stack) == []


if __name__ == '__main__':
    pytest.main()
