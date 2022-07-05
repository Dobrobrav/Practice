from typing import Callable, Union


class InputValues:
    _render: Union[Callable, Callable]  # mypy doesn't like single Callable

    def __init__(self, render: Callable):
        self._render = render

    def __call__(self, func) -> Callable:
        def wrapper(*args, **kwargs) -> list:
            return [self._render(elem) for elem in func().split()]

        return wrapper


class RenderDigit:
    def __call__(self, value: str, *args, **kwargs):
        return int(value) if self._is_intable(value) else None

    @staticmethod
    def _is_intable(value: str) -> bool:
        # return string.isdigit() or string[0] == "-" and string[1:].isdigit()
        try:
            int(value)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    render = RenderDigit()
    input_dg = InputValues(render)(input)
    res = input_dg()

    print(res)
