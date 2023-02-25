from typing import Optional, Iterable, List


class StackObj:
    """ Node for stack. """

    data: str
    next: 'Optional[StackObj]' = None

    def __init__(self, data: str):
        self.data = data

    def __repr__(self):
        return str(self.data)


class Stack:
    """ Stack-like structure. """

    top: Optional[StackObj] = None
    _length = 0

    def __add__(self, other: object) -> 'Stack':
        if not isinstance(other, StackObj):
            return NotImplemented
        self.push(other)
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

    def __setitem__(self, key: int, value: StackObj):
        self._check_index(key)

        if self._length == 1:
            self.top = value

        elif self._length >= 2:
            # if there are 2+ nodes, search for the node
            current = self.top
            for _ in range(key - 1):
                current = current.next

            if self._length - key == 1:  # if changing the latest added node
                current.next = value
            else:  # if there are nodes after the one being searched for
                if key == 0:
                    value.next = self.top.next
                    self.top = value
                else:  # if index != 0
                    next = current.next
                    current.next = value
                    value.next = next.next

    def __getitem__(self, item: int) -> 'StackObj':
        self._check_index(item)
        current = self.top
        for _ in range(item):
            current = current.next
        return current

    def __repr__(self):  # Stack([obj1.data, obj2.data, objN.data])
        return f"Stack({str(self._get_objects())})"

    def push(self, obj: StackObj) -> None:
        """ Add StackObj instance to the end of stack. """
        self._length += 1
        if self.top is None:  # if stack is empty
            self.top = obj
            return

        this_iteration_obj = self.top  # if stack is not empty
        while this_iteration_obj.next is not None:
            this_iteration_obj = this_iteration_obj.next
        this_iteration_obj.next = obj

    def pop(self) -> Optional[StackObj]:
        """ Delete and return the latest added StackObj. """
        if self.top is None:  # if the stack is empty
            return None

        self._length -= 1
        current_obj = self.top
        if current_obj.next is None:  # if there's only 1 node in the stack
            popped_obj = self.top
            self.top = None
            return popped_obj

        while current_obj.next.next is not None:  # if there're 2+ nodes in the stack
            current_obj = current_obj.next
        popped_obj = current_obj.next  # type: ignore
        current_obj.next = None
        return popped_obj

    def _get_objects(self) -> List[StackObj]:
        """ Return all objects in stack. """
        if self.top is None:
            return []

        objects = [self.top]
        current_obj = self.top
        while current_obj.next is not None:
            objects.append(current_obj.next)
            current_obj = current_obj.next
        return objects

    def _check_index(self, index: int):
        if self._length <= index:
            raise IndexError('неверный индекс')
