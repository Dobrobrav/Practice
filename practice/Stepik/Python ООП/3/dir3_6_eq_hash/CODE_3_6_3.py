class Rect:
    """ Class that represents a rectangle with:
     - coordinates of top-left point
     - width and height

    Rectangles with same width and height have the same hash.
    """

    _x: float
    _y: float
    _width: float
    _height: float

    def __init__(self, x: float, y: float, width: float, height: float):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __hash__(self):
        return hash((self._width, self._height))
