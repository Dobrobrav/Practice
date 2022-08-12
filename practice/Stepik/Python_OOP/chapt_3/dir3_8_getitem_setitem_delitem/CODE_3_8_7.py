class RadiusVector:
    """ Allows slices. """

    coords: list[float]

    def __init__(self, *args: float):
        self.coords = list(args)

    def __setitem__(self, key: int | slice, value: float):
        self.coords[key] = value

    def __getitem__(self, item: int | slice) -> tuple[float, ...]:
        res = self.coords[item]
        return tuple(res) if isinstance(res, list) else res

