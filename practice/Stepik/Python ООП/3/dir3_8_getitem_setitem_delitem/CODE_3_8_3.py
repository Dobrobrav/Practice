from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class CoordsAndSpeed:
    coords: Tuple[float, float]
    speed: float


class Track:
    start_x: float
    start_y: float
    linear_segments: List[CoordsAndSpeed]

    def __init__(self, start_x: int, start_y: int):
        self.linear_segments = []
        self.start_x = start_x
        self.start_y = start_y

    def add_point(self, x: float, y: float, speed: float):
        self.linear_segments.append(CoordsAndSpeed((x, y), speed))

    def __getitem__(self, item: int) -> Tuple[Tuple[float, float], float]:
        """ Return coords and speed. """
        self._check_index(item)
        return (self.linear_segments[item].coords,
                self.linear_segments[item].speed)  # type: ignore

    def __setitem__(self, key: int, value: float):
        """ Only change speed. """
        self._check_index(key)
        self.linear_segments[key].speed = value

    def _check_index(self, index: int):
        if not (isinstance(index, int)
                and 0 <= index <= len(self.linear_segments)):
            raise IndexError('некорректный индекс')
