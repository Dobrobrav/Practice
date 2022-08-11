from typing import List, Union, Callable


class InputDigits:
    _func: Union[Callable, Callable]

    def __init__(self, func: Callable):
        self._func = func

    def __call__(self) -> List[int]:
        input_var = self._func()
        return [int(x) for x in input_var.split()]


input_dg = InputDigits(input)
print(input_dg())
