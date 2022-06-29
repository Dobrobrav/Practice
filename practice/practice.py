from typing import TypeVar


T = TypeVar('T', int, str)


def foo(arg: T) -> T:
    return int(arg)


print(foo(3))
