from typing import List, Tuple, TypeAlias

Coord: TypeAlias = Tuple[float, float]


class PolyLine:
    """" Class representing polyline consisting of linear segments """

    _coords: List[Coord]

    def __init__(self, *args: Coord):
        self._coords = list(args)

    def add_coord(self, x: float, y: float) -> None:
        self._coords.append((x, y))

    def remove_coord(self, indx: int) -> Coord:
        return self._coords.pop(indx)

    def get_coords(self) -> List[Coord]:
        return self._coords
