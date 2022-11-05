from practice.Stepik.Python_OOP.c3_magic_methods.d9_iter_next \
    .code_8 import *


def get_nodes(stack: Stack) -> List[StackObj]:
    """ Return all nodes of stack. """
    if stack.top is None:
        return []

    objects = [stack.top]
    current_obj = stack.top
    while current_obj.next is not None:
        objects.append(current_obj.next)
        current_obj = current_obj.next
    return objects


def push_front(stack: Stack, obj: StackObj):
    """ Add StackObj to the beginning. """
    if not stack.top:  # empty stack
        stack.top = obj
    else:
        _push_front_in_filled_stack(stack, obj)
    stack._length += 1


def _push_front_in_filled_stack(stack: Stack, obj: StackObj):
    next_obj = stack.top
    obj.next = next_obj
    stack.top = obj


def push_back(stack: Stack, obj: StackObj):
    """ Add StackObj to the end. """
    stack._length += 1
    if not stack.top:
        return _push_back_in_empty_stack(stack, obj)
    _push_back_in_filled_stack(stack, obj)  # 1+ nodes in stack


def _push_back_in_empty_stack(stack: Stack, obj: StackObj):
    if stack.top is None:  # empty stack
        stack.top = obj


def _push_back_in_filled_stack(stack: Stack, obj: StackObj):
    current_node = stack.top  # not empty stack
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = obj
