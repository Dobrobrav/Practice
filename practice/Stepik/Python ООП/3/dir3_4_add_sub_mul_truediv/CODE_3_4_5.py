from typing import Callable


class ListMath:
    """ Class that changes functionality of regular lists
    in terms of arithmetical operational
    by allowing some new operations
    and redefining some others.
    """

    lst_math: list[float]

    def __init__(self, list_: list | None = None):
        if list_ is None:
            self.lst_math = []
        else:
            self.lst_math = [value for value in list_
                             if type(value) in (int, float)]

    def __repr__(self):  # [a, b, c] -> ListMath([a, b, c])
        return f"ListMath({str(self.lst_math)})"

    def __add__(self, other: float) -> 'ListMath':
        summary = self._get_result_of_operation(self.lst_math, other,
                                                lambda x, y: x + y)
        return ListMath(summary)

    def __radd__(self, other: float) -> 'ListMath':
        list_math_summary = self + other
        return list_math_summary

    def __iadd__(self, other: float) -> 'ListMath':
        summary = self._get_result_of_operation(self.lst_math, other,
                                                lambda x, y: x + y)
        self.lst_math = summary
        return self

    def __sub__(self, other: float):
        subtraction = self._get_result_of_operation(self.lst_math, other,
                                                    lambda x, y: x - y)
        return ListMath(subtraction)

    def __rsub__(self, other: float) -> 'ListMath':
        subtraction = self._get_result_of_operation(self.lst_math, other,
                                                    lambda x, y: y - x)
        return ListMath(subtraction)

    def __isub__(self, other: float) -> 'ListMath':
        difference = self._get_result_of_operation(self.lst_math, other,
                                                   lambda x, y: x - y)
        self.lst_math = difference
        return self

    def __mul__(self, other: float):
        product = self._get_result_of_operation(self.lst_math, other,
                                                lambda x, y: x * y)
        return ListMath(product)

    def __rmul__(self, other: float) -> 'ListMath':
        list_math_product = self * other
        return list_math_product

    def __imul__(self, other: float) -> 'ListMath':
        product = self._get_result_of_operation(self.lst_math, other,
                                                lambda x, y: x * y)
        self.lst_math = product
        return self

    def __truediv__(self, other: float):
        quotient = self._get_result_of_operation(self.lst_math, other,
                                                 lambda x, y: x / y)
        return ListMath(quotient)

    def __rtruediv__(self, other: float) -> 'ListMath':
        quotient = self._get_result_of_operation(self.lst_math, other,
                                                 lambda x, y: y / x)
        return ListMath(quotient)

    def __itruediv__(self, other: float) -> 'ListMath':
        quotient = self._get_result_of_operation(self.lst_math, other,
                                                 lambda x, y: x / y)
        self.lst_math = quotient
        return self

    @staticmethod
    def _get_result_of_operation(
            list_: list,
            number: float,
            operation: Callable,
    ) -> list[float]:
        result_of_operation = [round(operation(list_value, number), 13)
                               for list_value in list_]
        return result_of_operation
