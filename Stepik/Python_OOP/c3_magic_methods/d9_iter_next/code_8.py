from typing import Optional, Iterable, List


class StackObj:
    """ Node for stack. """

    data: str
    next: 'Optional[StackObj]' = None

    def __init__(self, data: str):
        self.data = data

    def __repr__(self):
        return f"obj: {self.data}"


class Stack:
    """ Stack-like structure. """

    top: Optional[StackObj] = None
    _length = 0

    def __add__(self, other: object) -> 'Stack':
        if not isinstance(other, StackObj):
            return NotImplemented
        self.push_back(other)
        return self

    def __iadd__(self, other: object) -> 'Stack':
        if not isinstance(other, StackObj):
            return NotImplemented
        return self + other

    def __mul__(self, other: Iterable[str]) -> 'Stack':
        for data in other:
            self + StackObj(data)
        return self

    def __imul__(self, other: Iterable[str]) -> 'Stack':
        return self * other

    def __setitem__(self, key: int, value: str):
        self._check_index(key)
        node = StackObj(value)

        if key == 0:  # and len(self) == 1
            self._change_first_node(node)
        elif len(self) >= 2:
            self._change_node_in_long_stack(key, node)

    def __getitem__(self, item: int) -> str:
        self._check_index(item)
        return self._get_node(item).data

    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self._length

    def __repr__(self):  # Stack([obj1.data, obj2.data, ..., objN.data])
        return f"Stack({str(self._get_nodes())})"

    def push_back(self, obj: StackObj):
        """ Add StackObj to the end. """
        self._length += 1
        if not self.top:
            return self._push_back_in_empty_stack(obj)
        self._push_back_in_filled_stack(obj)  # 1+ nodes in stack

    def push_front(self, obj: StackObj):
        """ Add StackObj to the beginning. """
        if not self.top:  # empty stack
            self.top = obj
        else:
            self._push_front_in_filled_stack(obj)
        self._length += 1

    def pop(self) -> Optional[StackObj]:
        if not self.top:  # empty stack
            return None

        self._length -= 1
        if self.top.next is None:  # 1 node in the stack
            return self._pop_from_one_node_stack()
        return self._pop_in_long_stack()  # 2+ nodes in the stack

    def _push_front_in_filled_stack(self, obj: StackObj):
        next_obj = self.top
        obj.next = next_obj
        self.top = obj

    def _push_back_in_empty_stack(self, obj: StackObj):
        if not self.top:  # empty stack
            self.top = obj

    def _push_back_in_filled_stack(self, obj: StackObj):
        current_node = self.top  # not empty stack
        while current_node.next:
            current_node = current_node.next
        current_node.next = obj

    def _pop_from_one_node_stack(self) -> StackObj:
        popped_node = self.top
        self.top = None
        return popped_node

    def _pop_in_long_stack(self) -> StackObj:
        current_node = self.top
        while current_node.next.next is not None:
            current_node = current_node.next
        popped_node = current_node.next
        current_node.next = None
        return popped_node

    def _change_first_node(self, node: StackObj):
        node.next = self.top.next
        self.top = node

    def _change_node_in_long_stack(self, key: int, node: StackObj):
        if len(self) - key == 1:  # changing the last node
            self._change_last_node(node)
        else:  # changing middle node
            self._change_middle_node(key, node)

    def _get_node(self, key: int) -> StackObj:
        node = self.top
        for _ in range(key):
            node = node.next
        return node

    def _change_last_node(self, node: StackObj):
        current = self._get_node(len(self) - 2)
        current.next = node

    def _change_middle_node(self, key: int, node: StackObj):
        current = self._get_node(key - 1)
        next_obj = current.next
        current.next = node
        node.next = next_obj.next

    def _get_nodes(self) -> List[StackObj]:
        """ Return all nodes of the stack. """
        if self.top is None:
            return []

        objects = [self.top]
        current_obj = self.top
        while current_obj.next is not None:
            objects.append(current_obj.next)
            current_obj = current_obj.next
        return objects

    def _check_index(self, index: int):
        if not (type(index) is int and 0 <= index < len(self)):
            raise IndexError('неверный индекс')
