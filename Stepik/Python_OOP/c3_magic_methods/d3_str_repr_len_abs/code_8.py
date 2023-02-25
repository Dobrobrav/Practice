class Clock:
    """ Contain time in hours, minutes and seconds. """

    _hours: int
    _minutes: int
    _seconds: int

    def __init__(self, hours: int, minutes: int, seconds: int):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def get_time(self) -> int:
        """ Return time in seconds. """
        return self._hours * 3600 + self._minutes * 60 + self._seconds


class DeltaClock:
    """ Calculate temporal difference between clock1 and clock2. """

    _clock1: Clock
    _clock2: Clock

    def __init__(self, clock1: Clock, clock2: Clock):
        self._clock1 = clock1
        self._clock2 = clock2

    def __str__(self):
        """ Return temporal difference in format <hh: mm: ss>."""
        delta_in_seconds = len(self)
        hours = delta_in_seconds // 3600
        minutes = delta_in_seconds % 3600 // 60
        seconds = delta_in_seconds % 3600 % 60
        return f"{hours:02}: {minutes:02}: {seconds:02}"

    def __len__(self):
        """ Return temporal difference in seconds. """
        delta_in_seconds = self._clock1.get_time() - self._clock2.get_time()
        return delta_in_seconds if delta_in_seconds > 0 else 0
