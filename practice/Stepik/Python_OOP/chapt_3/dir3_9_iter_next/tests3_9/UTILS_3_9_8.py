from practice.Stepik.Python_OOP.chapt_3.dir3_9_iter_next \
    .CODE_3_9_8 import *


def push_back(stack: Stack, obj: StackObj):
    """ Add StackObj to the end. """
    stack._length += 1
    if not stack.top:
        return _push_back_in_empty_stack(stack, obj)
    _push_back_in_filled_stack(stack, obj)  # 1+ nodes in stack


def get_nodes(stack: Stack) -> List[StackObj]:
    """ Return all nodes of the stack. """
    if stack.top is None:
        return []

    objects = [stack.top]
    current_obj = stack.top
    while current_obj.next is not None:
        objects.append(current_obj.next)
        current_obj = current_obj.next
    return objects


def _push_back_in_empty_stack(stack: Stack, obj: StackObj):
    if stack.top is None:  # empty stack
        stack.top = obj


def _push_back_in_filled_stack(stack: Stack, obj: StackObj):
    current_node = stack.top  # not empty stack
    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = obj
