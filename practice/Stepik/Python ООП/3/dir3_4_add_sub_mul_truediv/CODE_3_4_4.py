from typing import Optional, Union, TypeAlias, Any

Listable: TypeAlias = Union[list, 'NewList']


class NewList:
    _inner_list: list

    def __init__(self, list_: Optional[list] = None):
        self._inner_list = list_ or []

    def __sub__(self, other: Listable):  # NewList([a, b, c]) - <NewList([b, c, d]) or [b, c, d]>
        reduced = self.get_list()
        deductible = other if isinstance(other, list) else other.get_list()
        difference = self._get_difference_list(reduced, deductible)
        return NewList(difference)

    def __rsub__(self, other: list):  # [a, b, c] - NewList([b, c, d])
        reduced = other
        deductible = self.get_list()
        difference = self._get_difference_list(reduced, deductible)
        return NewList(difference)

    def __isub__(self, other: Listable):  # list_var -= <NewList([b, c, d]) or [b, c, d]>
        reduced = self.get_list()
        deductible = other if isinstance(other, list) else other.get_list()
        self._inner_list = self._get_difference_list(reduced, deductible)
        return self

    def __repr__(self):  # [a, b, c] -> NewList([a, b, c])
        return f"NewList({str(self.get_list())})"

    @classmethod
    def _get_difference_list(cls, reduced: list, deductible: list) -> list:
        """  Return resulting list after subtraction. """
        deductible = deductible.copy()
        difference = [
            elem for elem in reduced if not cls._find_in_list(elem, deductible)
        ]
        return difference

    @staticmethod
    def _find_in_list(value: Any, list_: list) -> bool:
        """ Return False if list_ doesn't contain value;
        Return True and REMOVE one instance of value from list_ if list_ contains value.
        """
        if all(value != list_elem or type(value) is not type(list_elem)
               for list_elem in list_):
            return False
        list_.remove(value)
        return True

    def get_list(self) -> list:
        return self._inner_list
