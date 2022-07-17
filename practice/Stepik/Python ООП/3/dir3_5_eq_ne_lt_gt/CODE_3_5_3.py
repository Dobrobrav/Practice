from math import sqrt


class TrackLine:
    """ Class representing point along track
     with coordinates and max speed by that point. """

    _to_x: float
    _to_y: float
    _max_speed: int

    def __init__(self, to_x: float, to_y: float, max_speed: int):
        self._to_x = to_x
        self._to_y = to_y
        self._max_speed = max_speed

    def __repr__(self):
        return f"({self._to_x}, {self._to_y})"

    @property
    def to_x(self):
        return self._to_x

    @property
    def to_y(self):
        return self._to_y


class Track:
    """ Class representing track with starting coordinates,
     joining points (class <TrackLine>) and current length. """

    _start_x: float
    _start_y: float
    _route: list[TrackLine]
    _current_length: float

    def __init__(self, start_x: float, start_y: float):
        self._route = [TrackLine(start_x, start_y, 0)]
        self._current_length = 0
        self._start_x = start_x
        self._start_y = start_y

    def __len__(self):
        """ Return length of track, parsed to int. """
        return int(self._current_length)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Track):
            return NotImplemented
        return len(self) == len(other)

    def __gt__(self, other: 'Track') -> bool:
        return len(self) > len(other)

    def __repr__(self):
        return f"{self._route}; length: {self._current_length}"

    def add_track(self, tr: TrackLine) -> None:
        self._current_length += sqrt(
            (tr.to_x - self._route[-1].to_x) ** 2
            + (tr.to_y - self._route[-1].to_y) ** 2
        )
        self._route.append(tr)

    def get_tracks(self) -> tuple[TrackLine, ...]:
        return tuple(self._route)


if __name__ == '__main__':
    track1 = Track(0, 0)
    track2 = Track(0, 1)

    track1.add_track(TrackLine(2, 4, 100))
    track1.add_track(TrackLine(5, -4, 100))

    track2.add_track(TrackLine(3, 2, 90))
    track2.add_track(TrackLine(10, 8, 90))

    res_eq = track1 == track2
    print(res_eq)
