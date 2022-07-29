from typing import Optional, Tuple


class Ellipse:
    """
    x1, y1 - top left angle coordinates;
    x2, y2 - bottom right angle coordinates.
    """

    x1: float
    y1: float
    x2: float
    y2: float

    def __init__(self,
                 x1: Optional[float] = None, y1: Optional[float] = None,
                 x2: Optional[float] = None, y2: Optional[float] = None):
        if (not all(coord is None for coord in (x1, y1, x2, y2))
                and any(coord is None for coord in (x1, y1, x2, y2))):
            raise AttributeError('type either all coordinates or none of them')

        if all(coord is not None for coord in (x1, y1, x2, y2)):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2

    def __bool__(self):
        """ Return True if all 4 coordinates are defined. """
        return set(self.__dict__.keys()) >= {'x1', 'y1', 'x2', 'y2'}

    def get_coords(self) -> Tuple[float, ...]:
        try:
            return self.x1, self.y1, self.x2, self.y2
        except AttributeError:
            raise AttributeError('нет координат для извлечения')


if __name__ == '__main__':
    lst_geom = [
        Ellipse(),
        Ellipse(1, 2, 3, 4),
        Ellipse(),
        Ellipse(4, 3, 2, 1),
    ]

    for ellipse in lst_geom:
        if ellipse:
            ellipse.get_coords()
