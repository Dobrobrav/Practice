from typing import Tuple, List, Optional
from math import sqrt


class RadiusVector:
    """ n-dimensional radius vector. """

    _coords: Optional[List[float]] = None

    def __init__(self, *args):
        if len(args) == 1:
            self._coords = [0 for _ in range(args[0])]
        elif len(args) > 1:
            self._coords = list(args)

    def __len__(self) -> Optional[int]:
        return 0 if self._coords is None else len(self._coords)

    def __abs__(self):
        if self._coords is None:
            return 0
        return sqrt(sum(coord ** 2 for coord in self._coords))

    def set_coords(self, *args) -> None:
        if len(args) == 1:
            args = tuple(0 for _ in range(args[0]))
        if self._coords is None:
            self._coords = list(args)
        for indx, coord in enumerate(args):
            self._coords[indx] = coord

    def get_coords(self) -> Optional[Tuple[float, ...]]:
        return tuple(self._coords)
