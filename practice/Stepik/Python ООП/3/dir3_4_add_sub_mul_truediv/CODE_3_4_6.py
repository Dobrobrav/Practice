from typing import Iterable


class StackObj:
    """ Class that represents nodes of Stack. """

    __data: str
    __next: 'StackObj | None' = None

    def __init__(self, data: str):
        self.__data = data

    def __repr__(self):
        return str(self.__data)

    @property
    def next(self) -> 'StackObj | None':
        return self.__next

    @next.setter
    def next(self, obj: 'StackObj | None'):
        self.__next = obj


class Stack:
    """ Class that represents stack-like structure. """

    top: StackObj | None = None

    def __repr__(self):  # Stack([obj1.data, obj2.data, objN.data])
        return f"Stack({str(self._get_objects())})"

    def __add__(self, other: StackObj) -> 'Stack':
        self.push_back(other)
        return self

    def __iadd__(self, other: StackObj) -> 'Stack':
        return self + other

    def __mul__(self, other: Iterable[str]) -> 'Stack':
        for data in other:
            self + StackObj(data)
        return self

    def __imul__(self, other: Iterable[str]) -> 'Stack':
        return self * other

    def push_back(self, obj: StackObj) -> None:
        """ Add StackObj instance to the end of stack. """
        if self.top is None:
            self.top = obj
            return

        this_iteration_obj = self.top
        while this_iteration_obj.next is not None:
            this_iteration_obj = this_iteration_obj.next
        this_iteration_obj.next = obj

    def pop_back(self) -> 'StackObj | None':
        """ Delete and return the latest added StackObj instance. """
        if self.top is None:  # if the stack is empty
            return None

        current_obj = self.top
        if current_obj.next is None:  # if the stack has only 1 node
            popped_obj = self.top
            self.top = None
            return popped_obj

        while current_obj.next.next is not None:  # if the stack has 2+ nodes
            current_obj = current_obj.next
        popped_obj = current_obj.next
        current_obj.next = None
        return popped_obj

    def _get_objects(self) -> list[StackObj]:
        if self.top is None:
            return []

        objects = [self.top]
        current_obj = self.top
        while current_obj.next is not None:
            objects.append(current_obj.next)
            current_obj = current_obj.next
        return objects
