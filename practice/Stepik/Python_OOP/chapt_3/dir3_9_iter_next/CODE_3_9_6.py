from typing import Iterator


class TriangleListIterator:
    lst: list[list]

    def __init__(self, lst: list[list]):
        self.lst = lst

    def __iter__(self) -> Iterator:
        """ Iterate a 2D-array triangle-wize.
        If not possible, IndexError will be naturally raised.
        """
        for i, row in enumerate(self.lst, start=1):
            for j in range(i):
                yield row[j]


