from typing import List, Union, Tuple


class Track:
    __points: 'List[PointTrack]'

    def __init__(self, *args: Union[float, 'PointTrack']):
        """ Take either coordinates x, y (numbers) of one PointTrack instance,
        or as many PointTrack instances as needed.
        """
        self._validate_args(*args)
        if self._is_only_one_point(*args):
            self.__points = [PointTrack(*args)]  # type: ignore
        else:
            self.__points = list(args)  # type: ignore

    def add_back(self, pt: 'PointTrack'):
        self.__points.append(pt)

    def add_front(self, pt: 'PointTrack'):
        self.__points.insert(0, pt)

    def pop_back(self) -> 'PointTrack':
        """Remove and return last item.
        Raises IndexError if track is empty.
        """
        return self.__points.pop()

    def pop_front(self) -> 'PointTrack':
        """Remove and return first item.
        Raises IndexError if track is empty.
        """
        return self.__points.pop(0)

    @property
    def points(self) -> Tuple['PointTrack', ...]:
        return tuple(self.__points)

    @staticmethod
    def _validate_args(*args: Union[float, 'PointTrack']):
        is_one_point = (len(args) == 2
                        and all(type(x) in (int, float) for x in args))
        is_many_points = all(isinstance(x, PointTrack) for x in args)
        if not (is_one_point or is_many_points):
            raise TypeError("pass either coordinates x, y (numbers) "
                            "of one PointTrack, "
                            "or as many PointTrack instances as needed.")

    @staticmethod
    def _is_only_one_point(*args: Union[float, 'PointTrack']) -> bool:
        return len(args) == 2 and type(args[0]) in (int, float)


class PointTrack:
    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        self._validate_coords(x, y)
        self._x = x
        self._y = y

    def __repr__(self):
        return f"PointTrack: {self._x}, {self._y}"

    @staticmethod
    def _validate_coords(x: float, y: float):
        if any(type(coord) not in (int, float) for coord in (x, y)):
            raise TypeError('координаты должны быть числами')
